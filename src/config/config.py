from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:
    def __init__(self) -> None:
        self.__connection_string = 'postgresql+pg8000://root:password@postgresdb/default'
        self.session = None

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind = engine)
        return self
    
    def __exit__(self, exec_type, exec_val, exec_tb):
        self.session.close()
        