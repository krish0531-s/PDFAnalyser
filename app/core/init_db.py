from app.core.database import Base
from app.core.database import engine

from app.models.document import Document

Base.metadata.create_all(bind=engine)