from fastapi import APIRouter
from models.char import Char

router = APIRouter()

chars_db = [] # temporary until db is setup

@router.post("/chars", response_model=Char)
async def create_char(char: Char):
    chars_db.append(char)
    return char

@router.get("/chars/")
async def read_chars():
    return chars_db

@router.get("/chars/{char_id}", response_model=Char)
async def read_char(char_id: int):
    for char in chars_db:
        if char_id == char.id:
            return char
    return None # throw error here

@router.delete('/chars/{char_id}')
async def delete_char(char_id: int):
    for index, char in chars_db:
        if char_id == char.id:
            chars_db.remove(index)
            return
    return None # throw error here
    