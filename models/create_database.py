from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from models import Base
#Load env
# Install 'psycopg2' if it require
load_dotenv()

database_url= f"postgresql://{os.getenv('userdb')}:{os.getenv('password')}@localhost:5432/test_db_fast_api"

engine = create_engine(database_url)
session_local = sessionmaker(bind=engine, autoflush=False) 
Base.metadata.create_all(bind=engine)





