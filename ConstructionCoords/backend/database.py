import os

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session, DeclarativeMeta


engine: Engine = create_engine(f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_ENDPOINT']}/construction_coords")
SessionLocal: sessionmaker[Session] = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db  # Hands the session to the route, then resumes here after the route completes
    finally:
        db.close()
