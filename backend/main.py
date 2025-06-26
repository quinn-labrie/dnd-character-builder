from fastapi import FastAPI
from routers import chars, users
from database import engine, Base, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(chars.router)
app.include_router(users.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
