import sys
from pathlib import Path

# Add the project's root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import uvicorn
from fastapi import Depends, FastAPI
from code.routes.pun_route import router as pun_router
from code.config.auth.users_route import router as auth_router
import os

app = FastAPI()
app.include_router(pun_router)
app.include_router(auth_router)

# if __name__ == "__main__":
#     print(os.getcwd())
#     uvicorn.run("main:app", host="127.0.0.1", port=8000)