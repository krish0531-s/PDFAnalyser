from enum import Enum


class DocumentStatus(str, Enum):
    UPLOADED = "uploaded" 


    EXTRACTING = "extracting"

    PROCESSED = "processed"

    FAILED = "failed"