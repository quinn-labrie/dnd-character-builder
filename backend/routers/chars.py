from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.char import CharCreate, CharResponse, Char

router = APIRouter()


@router.post("/chars/", response_model=CharResponse)
async def create_char(char: CharCreate, db: Session = Depends(get_db)):
    db_char = Char(name=char.name, owner_id=char.owner_id)
    db.add(db_char)
    db.commit()
    db.refresh(db_char)
    return db_char


@router.get("/chars/")
async def read_chars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    chars = db.query(Char).offset(skip).limit(limit).all()
    return chars
