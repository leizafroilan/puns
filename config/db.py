
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    # DB running on my VM for testing
    "mssql+pyodbc://sa:Just4Fun!@192.168.1.29:1433/PunsDB?driver=ODBC+Driver+17+for+SQL+Server", 
    fast_executemany=True,
    echo=True
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()