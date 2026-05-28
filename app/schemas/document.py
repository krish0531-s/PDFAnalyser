# from pydantic import BaseModel


# class DocumentCreate(BaseModel):
#     filename: str


# class DocumentResponse(BaseModel):
#     id: int
#     filename: str
#     status: str

#     model_config = {
#         "from_attributes": True
#     }


from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    filename: str
    stored_filename: str
    status: str

    model_config = {
        "from_attributes": True
    }