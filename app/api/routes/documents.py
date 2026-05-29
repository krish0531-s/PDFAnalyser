from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.processors.file_processor import FileProcessor
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService
from app.processors.pdf_processor import PDFProcessor
from app.repositories.document_extraction_repository import (
    DocumentExtractionRepository,
)

from app.services.document_extraction_service import (
    DocumentExtractionService,
)

from app.services.ai.mock_provider import MockProvider

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    repository = DocumentRepository(db)

    file_processor = FileProcessor()

    pdf_processor = PDFProcessor()

    service = DocumentService(
        repository=repository,
        file_processor=file_processor,
        pdf_processor=pdf_processor,
    )

    document = service.upload_document(file)

    return document


@router.post("/{document_id}/process")
async def process_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    repository = DocumentRepository(db)

    file_processor = FileProcessor()

    pdf_processor = PDFProcessor()

    service = DocumentService(
        repository=repository,
        file_processor=file_processor,
        pdf_processor=pdf_processor,
    )

    document = service.process_document(document_id)

    return document

@router.post("/{document_id}/extract")
async def extract_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document_repository = DocumentRepository(db)

    extraction_repository = (
        DocumentExtractionRepository(db)
    )

    provider = MockProvider()

    service = DocumentExtractionService(
        document_repository=document_repository,
        extraction_repository=extraction_repository,
        ai_provider=provider,
    )

    return service.extract_document(document_id)