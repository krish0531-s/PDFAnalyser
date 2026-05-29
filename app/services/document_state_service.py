from app.models.document import Document
from app.models.document_status import DocumentStatus


class DocumentStateService:

    @staticmethod
    def mark_extracting(document: Document) -> None:
        document.status = DocumentStatus.EXTRACTING

    @staticmethod
    def mark_processed(document: Document) -> None:
        document.status = DocumentStatus.PROCESSED

    @staticmethod
    def mark_failed(document: Document) -> None:
        document.status = DocumentStatus.FAILED