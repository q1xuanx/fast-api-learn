from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 

load_dotenv()

database_url = os.getenv('database_url')

engine = create_engine(database_url) 
SessionLocal = sessionmaker(bind=engine, autoflush=True)

def get_db(): 
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()
