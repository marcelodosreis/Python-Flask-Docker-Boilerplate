from src.config.config import DBConnection
from src.entities.users import Users as UsersModel

class UserRepository:
    def insert_user(self, name):
        with DBConnection() as db:
            new_user = UsersModel(name=name)
            db.session.add(new_user)
            db.session.commit()