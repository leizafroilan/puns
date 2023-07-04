from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from typing import List
from code.crud.pun_crud import get_random_pun, create_pun, get_all
from code.config.db import get_db
from code.models.pun_model import PunCreate, PunDisplay


router = APIRouter(
    prefix="/puns",
    tags=["puns"],
)

@router.get("/get_rnd_pun")
async def get_rnd_pun(db: Session = Depends(get_db)):
    result = await get_random_pun(db)
    return jsonable_encoder(result)

@router.get("/get_all",
            response_class=ORJSONResponse,
            # response_model=List[PunDisplay]
            )
async def get_all_puns(db: Session = Depends(get_db)):
    result = await get_all(db)
    response_data = {
        "Status": result["Status"],
        "Message": jsonable_encoder(result["Message"])
    }
    return ORJSONResponse(content=response_data)

@router.post("/create",
        #    response_model=PunDisplay
          )
async def create_user(pun: PunCreate, db: Session = Depends(get_db)):
    result = await create_pun(db, pun.Title, pun.Question, pun.Answer)
    return jsonable_encoder(result)
