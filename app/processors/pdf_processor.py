from pathlib import Path

import pdfplumber

from app.core.config import settings


class PDFProcessor:
    def extract_text(self, stored_filename: str) -> str:
        file_path = (
            Path(settings.upload_dir)
            / stored_filename
        )

        extracted_pages: list[str] = []

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    extracted_pages.append(text)

        return "\n".join(extracted_pages)