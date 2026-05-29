# from abc import ABC
# from abc import abstractmethod

# from app.schemas.extraction import DocumentExtraction


# class AIProvider(ABC):

#     provider_name: str

#     @abstractmethod
#     def extract(
#         self,
#         text: str,
#     ) -> DocumentExtraction:
#         pass

from abc import ABC
from abc import abstractmethod

from app.schemas.extraction import DocumentExtraction


class AIProvider(ABC):

    provider_name: str

    @abstractmethod
    def extract(
        self,
        text: str,
    ) -> DocumentExtraction:
        pass