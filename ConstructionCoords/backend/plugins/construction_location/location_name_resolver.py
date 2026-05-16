import json
import os
from json import JSONDecodeError
from pathlib import Path
from typing import Any

from openai import OpenAI


class LocationNameResolver:
    def __init__(self):
        self._client: OpenAI = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

    def assign_name_to_point(self, construction_location) -> None:
        prompt = self.construct_prompt(construction_location.latitude, construction_location.longitude)

        request: list[dict[str, str]] = [
            {
                "role": "system",
                "content": (
                    "You are a strict geospatial annotator for a JSON object. Based solely on "
                    "the coordinates provided, you assign concise English location names and calibrated "
                    "confidence scores, avoiding any guess that exceeds your actual certainty, and return "
                    "a validated JSON object that conforms exactly to the schema specified by the user."
                ),
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
            except JSONDecodeError:
                print(f"OpenAI invalid response format. Couldn't parse the JSON!\n'''\n{open_ai_response}\n'''")

    @staticmethod
    def construct_prompt(latitude: float, longitude: float) -> str:
        BASE_DIR = Path(__file__).resolve().parent
        PROMPT_TEMPLATE_FILE_PATH = BASE_DIR / "resources" / "prompt_template.xml"

        template: str = PROMPT_TEMPLATE_FILE_PATH.read_text(encoding="utf-8")
        content: str = f'{{"longitude": {longitude}, "latitude": {latitude}}}'

        return template.replace("{{content}}", content)

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
