from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:
    def __init__(self, db: Session):
        self.db = db

    # def create(self, filename: str, status: str) -> Document:
    #     document = Document(
    #         filename=filename,
    #         status=status,
    #     )

    #     self.db.add(document)
    #     self.db.commit()
    #     self.db.refresh(document)

    #     return document

    def create(
        self,
        filename: str,
        stored_filename: str,
        status: str,
    ) -> Document:
        document = Document(
            filename=filename,
            stored_filename=stored_filename,
            status=status,
        )

        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def get_by_id(self, document_id: int) -> Document | None:
        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )
    
    def update_extracted_text(
        self,
        document: Document,
        extracted_text: str,
    ) -> Document:
        document.extracted_text = extracted_text
        document.status = "processed"

        self.db.commit()
        self.db.refresh(document)

        return document