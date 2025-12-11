from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# without docker use 
# URL_DATABASE = 'postgresql://postgres@localhost:5432/starboy'
# with docker use
URL_DATABASE = os.getenv("DATABASE_URL", 'postgresql://postgres:elephant@db:5432/starboy')

engine = create_engine(URL_DATABASE)

SessionLocale = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()