from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 

load_dotenv()

database_url = f"postgresql://{os.getenv('userdb')}:{os.getenv('password')}@localhost:5432/test_db_fast_api"

engine = create_engine(database_url) 
SessionLocal = sessionmaker(bind=engine, autoflush=False)

def get_db(): 
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()