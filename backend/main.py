from fastapi import FastAPI
from routers import chars, users

app = FastAPI()
app.include_router(chars.router)
app.include_router(users.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
