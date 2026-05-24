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
        # Nominatim is the geocoding engine built on top of OpenStreetMap data.
        self._geolocator: Nominatim = Nominatim(user_agent="construction-coords")

    def annotate_location(self, construction_location) -> None:
        reverse_geocode_response: str | None = self._reverse_geocode(construction_location)
        print(f"--| OpenStreetMap response for [lat={construction_location.latitude}, lon={construction_location.longitude}]: \n'''\n{reverse_geocode_response}\n'''")

        prompt = self.construct_prompt(construction_location.latitude, construction_location.longitude, reverse_geocode_response)

        request: list[dict[str, str]] = [
            {
                "role": "system",
                "content": self.construct_system_instructions(reverse_geocode_response),
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
                print(f"--| OpenAI response for [lat={construction_location.latitude}, lon={construction_location.longitude}]:\n'''\n{json.dumps(parsed_open_ai_response, indent=2)}\n'''")

                construction_location.name = parsed_open_ai_response.get("name") or "N/A"
                construction_location.name_confidence = parsed_open_ai_response.get("name_confidence") or 0.0
                construction_location.type = parsed_open_ai_response.get("type") or "N/A"
                construction_location.visibility_level = parsed_open_ai_response.get("visibility_level") or "N/A"
                construction_location.description = parsed_open_ai_response.get("description") or "N/A"
            except JSONDecodeError:
                print(f"OpenAI invalid response format. Couldn't parse the JSON!\n'''\n{open_ai_response}\n'''")

    def _reverse_geocode(self, construction_location) -> str | None:
        try:
            location = self._geolocator.reverse(
                (construction_location.latitude, construction_location.longitude),
                language="en",
                timeout=5
            )
            return location.raw.get("address") if location else None
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"Nominatim reverse geocode failed: {e}")
            return None

    @staticmethod
    def construct_prompt(latitude: float, longitude: float, reverse_geocode: str | None) -> str:
        BASE_DIR = Path(__file__).resolve().parent
        PROMPT_WITHOUT_GEOCODE_FILE_PATH = BASE_DIR / "resources" / "prompt_without_geocode.xml"
        PROMPT_WITH_GEOCODE_FILE_PATH = BASE_DIR / "resources" / "prompt_with_geocode.xml"

        content: str = f'{{"longitude": {longitude}, "latitude": {latitude}}}'

        if reverse_geocode is not None and reverse_geocode != "":
            template: str = PROMPT_WITH_GEOCODE_FILE_PATH.read_text(encoding="utf-8")
            template = template.replace("{{reverse_geocode_context}}", f"""<reverse_geocode_context>
        The following structured address data was retrieved from OpenStreetMap from these coordinates.
        Treat as ground truth:
        {reverse_geocode}
    </reverse_geocode_context>""")
        else:
            template: str = PROMPT_WITHOUT_GEOCODE_FILE_PATH.read_text(encoding="utf-8")

        return template.replace("{{content}}", content)

    @staticmethod
    def construct_system_instructions(reverse_geocode_response: str | None) -> str:
        if reverse_geocode_response is None or reverse_geocode_response == "":
            return (
                    "You are a strict geospatial annotator for JSON objects. Based solely on the coordinates "
                    "provided, you assign concise English location names, calibrated confidence scores, "
                    "feature types, visibility levels, and brief contextual descriptions. You avoid any "
                    "inference that exceeds your actual certainty, and you return a validated JSON object "
                    "that conforms exactly to the schema specified by the user."
                )
        else:
            return (
                    "You are a strict geospatial annotator for JSON objects. You are provided with coordinates "
                    "and an authoritative reverse-geocoded address from OpenStreetMap, which you must treat as "
                    "ground truth and prioritize over any prior knowledge. Using this context, you assign "
                    "concise English location names, calibrated confidence scores, feature types, visibility "
                    "levels, and brief contextual descriptions. You avoid any inference that exceeds what the "
                    "provided address and coordinates support, and you return a validated JSON object that "
                    "conforms exactly to the schema specified by the user."
                )

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
