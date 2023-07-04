from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship

Base = declarative_base()

class UsersT(Base):
    __tablename__ = "Users"

    UserID = Column(Integer, index=True)
    Username = Column(String, primary_key=True, unique=True, index=True)
    Email = Column(String, unique=True, index=True)
   
    users = relationship("PunsT", back_populates="puns")


class PunsT(Base):
    __tablename__ = "Puns"

    ID = Column(Integer, primary_key=True, index=True)
    Title = Column(String, unique=True, index=True)
    Question = Column(String, unique=True, index=True)
    Answer = Column(String, index=True)
    Date_Created = Column(DATETIME, index=True)
    Created_By = Column(String, ForeignKey("Users.Username"))

    puns = relationship("UsersT", back_populates="users", foreign_keys=[Created_By])





