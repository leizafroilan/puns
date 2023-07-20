import uvicorn
from fastapi import Depends, FastAPI
from code.routes import pun_route
from code.config.auth import users_route

app = FastAPI()
app.include_router(pun_route.router)
app.include_router(users_route.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)