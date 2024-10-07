from pydantic import BaseModel

class FormData(BaseModel):
    username: str
    password: str
