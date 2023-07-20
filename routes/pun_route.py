from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from typing import List
import random
from code.crud.pun_crud import get_random_pun, create_pun, get_all, delete_pun
from code.config.db import get_db
from code.models.pun_model import PunCreate, PunDisplay, PunDelete
from code.config.auth.users_auth import get_current_active_user
from code.config.auth.users_model import User

router = APIRouter(
    prefix="/puns",
    tags=["puns"],
)

@router.get("/get_rnd_pun",
            response_class=ORJSONResponse)
            
async def route_get_rnd_pun(db: Session = Depends(get_db)):
    # Queries all from Puns DB
    results = await get_all(db)

    # Get all IDs
    result_json = jsonable_encoder(results)
    id_list = [ v for msg in result_json['Message'] for k, v in msg.items() if k == 'ID' ]

    # Get random ID from id_list
    random_id = random.choice(id_list)
    
    # Queries Puns DB using random ID
    result =  await get_random_pun(db, random_id)

    response_data = {
        "Status": result["Status"],
        "Message": jsonable_encoder(result["Message"])
    }

    return ORJSONResponse(content=response_data)

@router.get("/get_all",
            response_class=ORJSONResponse,
            )
async def route_get_all_puns(db: Session = Depends(get_db)):
    result = await get_all(db)
    response_data = {
        "Status": result["Status"],
        "Message": jsonable_encoder(result["Message"])
    }
    return ORJSONResponse(content=response_data)

@router.post("/create")
async def route_create_pun(pun: PunCreate, db: Session = Depends(get_db),
                current_user: User = Security(get_current_active_user, scopes=["rw"])):
  
    result = await create_pun(db, pun.Title, pun.Question, pun.Answer, current_user.Username)
    return jsonable_encoder(result)

@router.post("/delete")
async def route_delete_pun(pun: PunDelete, db: Session = Depends(get_db),
                current_user: User = Security(get_current_active_user, scopes=["rw"])):

    result = await delete_pun(db, pun.ID)
    return jsonable_encoder(result)
