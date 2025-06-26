from pydantic import BaseModel

class Char(BaseModel):
    id: int
    name: str