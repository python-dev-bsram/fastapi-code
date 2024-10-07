from pydantic import BaseModel

class Filterdata(BaseModel):

    search: str 
    limit: str 
    page: int

    
