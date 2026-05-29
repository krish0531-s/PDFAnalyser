import time
from google.genai.errors import ServerError

import json

from google import genai

from app.core.config import settings
from app.schemas.extraction import DocumentExtraction
from app.services.ai.base import AIProvider
from app.services.prompt_service import PromptService


class GeminiProvider(AIProvider):

    provider_name = "gemini"

    def __init__(
        self,
        prompt_service: PromptService,
    ):
        self.prompt_service = prompt_service

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def extract(
        self,
        text: str,
    ) -> DocumentExtraction:

        prompt_template = (
            self.prompt_service.load_prompt(
                "document_extraction.txt"
            )
        )

        prompt = f"""
{prompt_template}

DOCUMENT:

{text}
"""

        # response = self.client.models.generate_content(
        #     # model="gemini-2.5-flash",
        #     model=settings.gemini_model,
        #     contents=prompt,
        # )


        max_attempts = 3

        for attempt in range(max_attempts):
            try:
                response = self.client.models.generate_content(
                    model=settings.gemini_model,
                    contents=prompt,
                )

                break

            except ServerError:

                if attempt == max_attempts - 1:
                    raise

                wait_time = 2 ** attempt

                print(
                    f"Gemini unavailable. "
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

        # raise RuntimeError(
        #     f"Gemini returned: {repr(response.text)}"
        # )
        
        response_text = response.text.strip()

        if response_text.startswith("```json"):
            response_text = response_text[7:]

        if response_text.endswith("```"):
            response_text = response_text[:-3]

        response_text = response_text.strip()

        extraction_dict = json.loads(
            response_text
        )

        return DocumentExtraction.model_validate(
        extraction_dict
    )