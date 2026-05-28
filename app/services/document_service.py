# from app.repositories.document_repository import DocumentRepository


# class DocumentService:
#     def __init__(self, repository: DocumentRepository):
#         self.repository = repository

#     def create_document(self, filename: str):
#         return self.repository.create(
#             filename=filename,
#             status="uploaded",
#         )

from fastapi import UploadFile

from app.processors.file_processor import FileProcessor
from app.repositories.document_repository import DocumentRepository
from app.processors.pdf_processor import PDFProcessor


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
            status="uploaded",
        )
    
    def process_document(self, document_id: int):
        document = self.repository.get_by_id(document_id)

        if document is None:
            raise ValueError("Document not found")

        extracted_text = self.pdf_processor.extract_text(
            document.stored_filename
        )

        return self.repository.update_extracted_text(
            document=document,
            extracted_text=extracted_text,
        )