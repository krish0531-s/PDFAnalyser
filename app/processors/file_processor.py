from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.core.config import settings


class FileProcessor:
    ALLOWED_EXTENSIONS = {".pdf"}

    def save_upload(self, file: UploadFile) -> str:
        extension = Path(file.filename).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError("Invalid file type")

        unique_filename = f"{uuid4()}{extension}"

        upload_path = Path(settings.upload_dir) / unique_filename

        with open(upload_path, "wb") as buffer:
            buffer.write(file.file.read())

        return unique_filename