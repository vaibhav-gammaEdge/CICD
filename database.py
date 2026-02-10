from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine

# It gets 'DATABASE_URL' from the docker-compose environment section
# Fallback to local if running outside Docker
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:lap47@localhost:5432/postgres")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()