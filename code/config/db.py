
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB (MS SQL) running on my VM for testing
# engine = create_engine(
#     'mssql+pyodbc://sa:Just4Fun!@192.168.1.29:1433/PunsDB?driver=ODBC+Driver+17+for+SQL+Server', 
#     fast_executemany=True,
#     echo=True
#     )

# SQLite3 db running locally
engine = create_engine(
    'sqlite:///./PunDB.db', connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()