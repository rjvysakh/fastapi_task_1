from sqlalchemy.orm import Session

from fastapi_task_2.db.models.document import Document
from fastapi_task_2.db.models.user import User


def get_user(db: Session, user_id: int):
    """
    Retrieve a user by their unique identifier.
 
    :param db: SQLAlchemy database session
    :param user_id: Unique identifier of the user
    :return: User object or None if not found
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    """
    Retrieve a user by their username.

    :param db: SQLAlchemy database session
    :param username: Username of the user
    :return: User object or None if not found
    """
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, username: str, hashed_password: str):
    """
    Create a new user.

    :param db: SQLAlchemy database session
    :param username: Username of the new user
    :param hashed_password: Hashed password of the new user
    :return: Created User object
    """
    db_user = User(username=username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_document(db: Session, title: str, content: str, user_id: int):
    """
    Create a new document and add it to the database.

    :param db: SQLAlchemy database session
    :param title: Title of the document
    :param content: Content of the document
    :param user_id: ID of the user associated with the document
    :return: Created document details
    """
    db_document = Document(title=title, content=content, user_id=user_id)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
