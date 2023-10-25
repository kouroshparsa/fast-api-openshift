import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = os.getenv('POSTGRESQL_DATABASE')
db_user = os.getenv('POSTGRESQL_USER')
db_pass = os.getenv('POSTGRESQL_PASSWORD')
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@postgresql:5432/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
