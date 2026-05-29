from pydantic import BaseModel


class ExtractedEntity(BaseModel):
    value: str
    context: str


class ExtractedDate(BaseModel):
    date: str
    description: str


class ExtractedAction(BaseModel):
    action: str


class DocumentExtraction(BaseModel):
    companies: list[ExtractedEntity]

    important_dates: list[ExtractedDate]

    filing_deadlines: list[ExtractedDate]

    penalties: list[ExtractedEntity]

    required_actions: list[ExtractedAction]

    summary: str