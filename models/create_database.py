from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from models import Base

#Install 'psycopg2' if it require
load_dotenv()

database_url= os.getenv('database_url')

engine = create_engine(database_url)
session_local = sessionmaker(bind=engine, autoflush=True) 
Base.metadata.create_all(bind=engine)
print('Create success')




