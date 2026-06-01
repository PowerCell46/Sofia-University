import json
import os
from json import JSONDecodeError
from pathlib import Path
from typing import Any

from geopy import Nominatim
from geopy.exc import GeocoderServiceError, GeocoderTimedOut
from openai import OpenAI


class LocationMetadataResolver:
    def __init__(self):
        self._client: OpenAI = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))
        self._geolocator: Nominatim = Nominatim(user_agent="geo-ai")  # Nominatim is the geocoding engine built on top of OpenStreetMap data.
        resources_dir = Path(__file__).resolve().parent.parent / "resources"
        self._prompt_without_geocode: str = (resources_dir / "prompt_without_geocode.xml").read_text(encoding="utf-8")
        self._prompt_with_geocode: str = (resources_dir / "prompt_with_geocode.xml").read_text(encoding="utf-8")

    def annotate_location(self, geo_ai_point) -> None:
        reverse_geocode_response: str | None = self.reverse_geocode(geo_ai_point)
        print(f"--| OpenStreetMap response for [lat={geo_ai_point.latitude}, lon={geo_ai_point.longitude}]: \n'''\n{reverse_geocode_response}\n'''")

        prompt: str = self.construct_prompt(geo_ai_point.latitude, geo_ai_point.longitude, reverse_geocode_response)
        system_instructions: str = self.construct_system_instructions(reverse_geocode_response)

        request: list[dict[str, str]] = [
            {
                "role": "system",
                "content": system_instructions,
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = self._client.chat.completions.create(
            model=os.getenv("OPEN_AI_LLM_MODEL"),
            messages=request
        )

        open_ai_response = self.strip_llm_response_result(response.choices[0].message.content)
        if open_ai_response is not None:
            try:
                parsed_open_ai_response: dict[str, Any] = json.loads(open_ai_response)
                print(f"--| OpenAI response for [lat={geo_ai_point.latitude}, lon={geo_ai_point.longitude}]:\n'''\n{json.dumps(parsed_open_ai_response, indent=2, ensure_ascii=False)}\n'''")

                geo_ai_point.name = parsed_open_ai_response.get("name") or "N/A"
                geo_ai_point.name_confidence = parsed_open_ai_response.get("name_confidence") or 0.0
                geo_ai_point.type = parsed_open_ai_response.get("type") or "N/A"
                geo_ai_point.visibility_level = parsed_open_ai_response.get("visibility_level") or "N/A"
                geo_ai_point.description = parsed_open_ai_response.get("description") or "N/A"
            except JSONDecodeError:
                print(f"OpenAI invalid response format. Couldn't parse the JSON!\n'''\n{open_ai_response}\n'''")

    def reverse_geocode(self, geo_ai_point) -> str | None:
        try:
            location = self._geolocator.reverse(
                (geo_ai_point.latitude, geo_ai_point.longitude),
                language="en",
                timeout=5
            )
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"Nominatim reverse geocode failed: {e}")
            return None

        if location is None:
            return None

        address: dict | None = location.raw.get("address")
        if not address:
            return None

        try:
            return json.dumps(address, indent=2, ensure_ascii=False)
        except (TypeError, ValueError) as e:
            print(f"Failed to serialize reverse geocode address {address!r}: {e}")
            return None

    def construct_prompt(self, latitude: float, longitude: float, reverse_geocode: str | None) -> str:
        content: str = f'{{"longitude": {longitude}, "latitude": {latitude}}}'

        if reverse_geocode:
            template = self._prompt_with_geocode.replace("{{reverse_geocode_context}}", f"""<reverse_geocode_context>
        The following structured address data was retrieved from OpenStreetMap from these coordinates.
        Treat as ground truth:
        {reverse_geocode.replace("\n", "\n        ")}
    </reverse_geocode_context>""")
        else:
            template = self._prompt_without_geocode

        return template.replace("{{content}}", content)

    @staticmethod
    def construct_system_instructions(reverse_geocode_response: str | None) -> str:
        base = (
                "You are a strict geospatial annotator for JSON objects. You assign concise English "
                "location names, calibrated confidence scores, feature types, visibility levels, and "
                "brief contextual descriptions, and return a validated JSON object that conforms "
                "exactly to the schema specified by the user."
            )
        if reverse_geocode_response:
            addendum = (
                    " You are provided with an authoritative reverse-geocoded address from OpenStreetMap, "
                    "which you must treat as ground truth and prioritize over any prior knowledge. "
                    "Avoid any inference that exceeds what the provided address and coordinates support."
                )
        else:
            addendum = (
                    " Based solely on the coordinates provided, avoid any inference that exceeds "
                    "your actual certainty."
                )
        return base + addendum

    @staticmethod
    def strip_llm_response_result(llm_response: str) -> str | None:
        llm_response = llm_response.strip()
        first_open_brace_inx = llm_response.find('{')
        last_close_brace_inx = llm_response.rfind('}')

        if first_open_brace_inx == -1 or last_close_brace_inx == -1:
            print(f"OpenAI invalid response format. Cannot find opening and closing braces!\n'''\n{llm_response}\n'''")
            return None

        if first_open_brace_inx < last_close_brace_inx:
            return llm_response[first_open_brace_inx:last_close_brace_inx + 1]

        return llm_response
