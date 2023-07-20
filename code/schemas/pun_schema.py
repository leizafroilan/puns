from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"

    Username = Column(String, primary_key=True, unique=True, index=True)
    Full_Name = Column(String, index=True)
    Hashed_Password = Column(String, index=True)
    Email = Column(String, unique=True, index=True)
    Scopes = Column(String, unique=True, index=True)
    Disabled = Column(Integer, index=True)
   
    users = relationship("Puns", back_populates="puns")


class Puns(Base):
    __tablename__ = "Puns"

    ID = Column(Integer, primary_key=True, index=True)
    Title = Column(String, unique=True, index=True)
    Question = Column(String, unique=True, index=True)
    Answer = Column(String, index=True)
    Date_Created = Column(DATETIME, index=True)
    Created_By = Column(String, ForeignKey("Users.Username"))

    puns = relationship("Users", back_populates="users", foreign_keys=[Created_By])





