from fastapi import APIRouter
from models.user import User

router = APIRouter()

users_db = []

@router.post("/users/", response_model=User)
async def create_user(user: User):
    users_db.append(user)
    return user

@router.get("/users/")
async def read_users():
    return users_db

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    return None  # throw error here