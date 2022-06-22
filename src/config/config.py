# Core
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Libs
import os


class DBConnection:

    def __init__(self) -> None:
        self.__connection_string = f'postgresql+pg8000://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("POSTGRES_DB")}'
        self.session = None
    
    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        