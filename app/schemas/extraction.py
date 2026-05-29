from pydantic import BaseModel


class ExtractedEntity(BaseModel):
    value: str


class ExtractedDate(BaseModel):
    value: str


class ExtractedAction(BaseModel):
    description: str


class DocumentExtraction(BaseModel):
    companies: list[ExtractedEntity]

    important_dates: list[ExtractedDate]

    filing_deadlines: list[ExtractedDate]

    penalties: list[ExtractedEntity]

    required_actions: list[ExtractedAction]

    summary: str