# # # # from fastapi import FastAPI

# # # # app = FastAPI(title="PDF Analyser")


# # # # @app.get("/")
# # # # async def root():
# # # #     return {"status": "ok"}
# # # from fastapi import FastAPI

# # # from app.api.routes.health import router as health_router

# # # app = FastAPI(title="PDF Analyser")

# # # app.include_router(health_router)
# # from fastapi import FastAPI

# # from app.api.routes.health import router as health_router
# # from app.core.init_db import Base
# # from app.core.init_db import engine

# # app = FastAPI(title="PDF Analyser")

# # app.include_router(health_router)

# # Base.metadata.create_all(bind=engine)
# from fastapi import FastAPI

# from app.api.routes.health import router as health_router

# app = FastAPI(title="PDF Analyser")

# app.include_router(health_router)

from fastapi import FastAPI

from app.api.routes.documents import router as documents_router
from app.api.routes.health import router as health_router

app = FastAPI(title="PDF Analyser")

app.include_router(health_router)
app.include_router(documents_router)