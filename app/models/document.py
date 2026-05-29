from sqlalchemy import Integer
from sqlalchemy import String, Text, Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.document_status import DocumentStatus

from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    filename: Mapped[str] = mapped_column(String, nullable=False)

    stored_filename: Mapped[str] = mapped_column(String, nullable=False)

    status: Mapped[str] = mapped_column(String, nullable=False)
    
    extracted_text: Mapped[str | None] = mapped_column(
    Text,
    nullable=True,
)