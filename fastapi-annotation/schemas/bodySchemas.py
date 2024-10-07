from  pydantic import BaseModel

class BodyData(BaseModel):
    username: str 
    password: str 
