# from app.schemas.extraction import (
#     DocumentExtraction,
#     ExtractedAction,
#     ExtractedDate,
#     ExtractedEntity,
# )

# from app.services.ai.base import AIProvider


# class MockProvider(AIProvider):

#     def extract(
#         self,
#         text: str,
#     ) -> DocumentExtraction:

#         return DocumentExtraction(
#             companies=[
#                 ExtractedEntity(
#                     value="Mock Company"
#                 )
#             ],
#             important_dates=[],
#             filing_deadlines=[],
#             penalties=[],
#             required_actions=[
#                 ExtractedAction(
#                     description="Mock action"
#                 )
#             ],
#             summary="Mock summary",
#         )


from app.schemas.extraction import (
    DocumentExtraction,
    ExtractedAction,
    ExtractedDate,
    ExtractedEntity,
)

from app.services.ai.base import AIProvider


class MockProvider(AIProvider):

    provider_name = "mock"

    def extract(
        self,
        text: str,
    ) -> DocumentExtraction:

        return DocumentExtraction(
            companies=[
                ExtractedEntity(
                    value="Mock Company",
                    context="Example company",
                )
            ],
            important_dates=[
                ExtractedDate(
                    date="2026-01-01",
                    description="Mock important date",
                )
            ],
            filing_deadlines=[
                ExtractedDate(
                    date="2026-01-31",
                    description="Mock filing deadline",
                )
            ],
            penalties=[
                ExtractedEntity(
                    value="$1000",
                    context="Mock penalty",
                )
            ],
            required_actions=[
                ExtractedAction(
                    action="Submit annual filing",
                )
            ],
            summary="Mock summary",
        )