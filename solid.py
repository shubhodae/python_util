from abc import ABC, abstractmethod

from sqlalchemy import create_engine, String
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

import logging

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# DB session
def get_db_session():
    engine = create_engine('sqlite:///test.db', echo=True)
    return Session(engine)

# Base class
class Base(DeclarativeBase):
    pass


# User table
class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(30), primary_key=True)
    password: Mapped[str] = mapped_column(String(30))
    email: Mapped[str]

    def __repr__(self) -> str:
        return f'{self.username} -> {self.email}'



class CreateUser:

    def create_user(self, username, password, email):
        user = {
            "username": username,
            "password": password,
            "email": email
        }

        with get_db_session() as session:
            user_obj = User(**user)
            session.add(user_obj)
            session.commit()

        print("user created")


class Email:

    def send_email(self, email):
        print(f"Email send to {email}")


class ErrorHandler(ABC):

    @abstractmethod
    def log_error(self, err):
        pass


class ErrorLogger(ErrorHandler):

    def log_error(self, err):
        logger.exception(err)
        print("Error logged !!!!!!!!!")


class FileErrorLogger(ErrorHandler):

    def log_error(self, err):
        print("Logging error in file !!!")


class CloudErrorLogger(ErrorHandler):

    def log_error(self, err):
        print("Logging error in cloud")



class UserRegistration:

    def register_user(self, name, password, email):
        try:
            CreateUser().create_user(name, password, email)
            Email().send_email(email)
        except Exception as e:
            ErrorLogger().log_error(e)
            FileErrorLogger().log_error(e)
            CloudErrorLogger().log_error(e)



if __name__ == "__main__":
    print("Hello S.O.L.I.D !")

    # engine = create_engine('sqlite:///test.db', echo=True)
    # Base.metadata.create_all(engine, tables=[User.__table__], checkfirst=True)

    UserRegistration().register_user(
        "shubho",
        "topsecret",
        "shubho@gmail.com"
    )
