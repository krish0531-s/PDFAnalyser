from fastapi import UploadFile

from app.processors.file_processor import FileProcessor
from app.repositories.document_repository import DocumentRepository
from app.processors.pdf_processor import PDFProcessor
from app.models.document_status import DocumentStatus



class DocumentService:
    def __init__(
        self,
        repository: DocumentRepository,
        file_processor: FileProcessor,
        pdf_processor: PDFProcessor,
    ):
        self.repository = repository
        self.file_processor = file_processor
        self.pdf_processor = pdf_processor

    def upload_document(self, file: UploadFile):
        stored_filename = self.file_processor.save_upload(file)

        return self.repository.create(
            filename=file.filename,
            stored_filename=stored_filename,
            status=DocumentStatus.UPLOADED.value,
        )
    
    def process_document(self, document_id: int):
        document = self.repository.get_by_id(document_id)

        if document is None:
            raise ValueError("Document not found")

        self.repository.update_status(
            document=document,
            status=DocumentStatus.EXTRACTING.value,
        )

        try:
            extracted_text = self.pdf_processor.extract_text(
                document.stored_filename
            )

            return self.repository.update_extracted_text(
                document=document,
                extracted_text=extracted_text,
            )

        except Exception:
            self.repository.update_status(
                document=document,
                status=DocumentStatus.FAILED.value,
            )

            raise