from app.schemas.extraction import (
    DocumentExtraction,
    ExtractedAction,
    ExtractedDate,
    ExtractedEntity,
)

from app.services.ai.base import AIProvider


class MockProvider(AIProvider):

    def extract(
        self,
        text: str,
    ) -> DocumentExtraction:

        return DocumentExtraction(
            companies=[
                ExtractedEntity(
                    value="Mock Company"
                )
            ],
            important_dates=[],
            filing_deadlines=[],
            penalties=[],
            required_actions=[
                ExtractedAction(
                    description="Mock action"
                )
            ],
            summary="Mock summary",
        )