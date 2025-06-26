from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel


class Char(Base):
    __tablename__ = "chars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="chars")


class CharCreate(BaseModel):
    name: str
    owner_id: int


class CharResponse(BaseModel):
    id: int
    name: str
    owner_id: int

    class Config:
        orm_mode = True
