import json

from sqlalchemy.orm import Session

from app.models.document_extraction import DocumentExtraction
from app.schemas.extraction import DocumentExtraction as ExtractionSchema


class DocumentExtractionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        document_id: int,
        provider: str,
        extraction: ExtractionSchema,
    ) -> DocumentExtraction:

        record = DocumentExtraction(
            document_id=document_id,
            provider=provider,
            summary=extraction.summary,
            extraction_json=extraction.model_dump_json(),
        )

        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)

        return record