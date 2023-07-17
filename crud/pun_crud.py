
from sqlalchemy.orm import Session
from datetime import datetime
from code.config.db import get_db
from code.schemas.pun_schema import Users, Puns


async def get_random_pun(db: Session, random_id):
    try:
        query = db.query(Puns).filter(Puns.ID == random_id).first()
        return {
            "Result": "Success",
            "Message": query,
            "Status": 200
        }

    except Exception as e:
        return {
            "Result": "Failed",
            "Message": str(e),
            "Status": 500
        }
    
async def get_all(db: Session):

    try:
        query = db.query(Puns).order_by(Puns.ID).offset(0).limit(100).all()

        return {
            "Result": "Success",
            "Message": query,
            "Status": 200
        }

    except Exception as e:
        return {
            "Result": "Failed",
            "Message": str(e),
            "Status": 500
        }        

    try:
        query = db.query(Puns).order_by(Puns.ID).offset(0).limit(100).all()

        return {
            "Result": "Success",
            "Message": query,
            "Status": 200
        }

    except Exception as e:
        return {
            "Result": "Failed",
            "Message": str(e),
            "Status": 500
        }

async def create_pun(db: Session, title, question, answer, d: datetime = datetime.now() ):


    try:
        db_item = Puns(Created_By="admin", Title=title, Question=question, Answer=answer, Date_Created=d)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return {
            "Result": "Success",
            "Message": "Item has been successfully added to DB",
            "Status": 201
        }

    except Exception as e:
        return {
            "Result": "Fail",
            "Message": str(e),
            "Status": 500
        }

