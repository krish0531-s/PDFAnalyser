from pydantic import BaseModel

from app.schemas.extraction import DocumentExtraction


class DocumentExtractionResponse(BaseModel):
    id: int
    document_id: int
    provider: str
    summary: str
    extraction: DocumentExtraction  