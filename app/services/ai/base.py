from abc import ABC
from abc import abstractmethod

from app.schemas.extraction import DocumentExtraction


class AIProvider(ABC):

    @abstractmethod
    def extract(
        self,
        text: str,
    ) -> DocumentExtraction:
        pass