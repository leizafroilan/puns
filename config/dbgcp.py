from google.cloud.sql.connector import Connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pyodbc

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pyodbc.Connection:
    conn: pyodbc.Connection = connector.connect(
        "festive-post-391811:asia-southeast1:ms-sql-express-01",
        "pyodbc",
        user="sqlserver",
        password="29QuoV@clxJust4Fun!",
        db="PunsDB"
    )
    return conn

# Create the engine using the Cloud SQL Connector
engine = create_engine('mssql+pyodbc://', creator=getconn, fast_executemany=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
