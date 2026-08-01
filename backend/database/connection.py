from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.settings import settings


engine = create_engine(settings.DATABASE_URL, echo=settings.APP_ENV == "development")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
