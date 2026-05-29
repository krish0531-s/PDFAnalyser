from app.repositories.document_repository import DocumentRepository
from app.repositories.document_extraction_repository import (
    DocumentExtractionRepository,
)

from app.services.ai.base import AIProvider


class DocumentExtractionService:

    def __init__(
        self,
        document_repository: DocumentRepository,
        extraction_repository: DocumentExtractionRepository,
        ai_provider: AIProvider,
    ):
        self.document_repository = document_repository
        self.extraction_repository = extraction_repository
        self.ai_provider = ai_provider

    def extract_document(
        self,
        document_id: int,
    ):
        document = self.document_repository.get_by_id(
            document_id
        )

        if document is None:
            raise ValueError("Document not found")

        if not document.extracted_text:
            raise ValueError(
                "Document has not been processed"
            )

        extraction = self.ai_provider.extract(
            document.extracted_text
        )

        return self.extraction_repository.create(
            document_id=document.id,
            provider=self.ai_provider.provider_name,
            extraction=extraction,
        )