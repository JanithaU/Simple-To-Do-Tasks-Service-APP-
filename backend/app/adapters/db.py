from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

# Database connection setup
from app.config import DATABASE_URL
# Set up logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to connect to the database
try:
    engine = create_engine(DATABASE_URL)
    # Optionally, test the connection by running a simple query
    with engine.connect() as connection:
        logger.info("Database connection established successfully.")
except SQLAlchemyError as e:
    logger.error(f"Database connection failed: {e}")
except Exception as e:
    logger.error(f"An unexpected error occurred while connecting to the database: {e}")


try:
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    logger.info("Database session created successfully.")
except Exception as e:
    logger.error(f"An unexpected error occurred while creating the session: {e}")



Base = declarative_base()
