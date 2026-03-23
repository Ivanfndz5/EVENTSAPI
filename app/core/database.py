from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = 'sqlite:///./app.db'

# Mas adelante podemos cambiar a Postgres sin tocar el resto del codigo

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False} #Solo para sqlite
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


