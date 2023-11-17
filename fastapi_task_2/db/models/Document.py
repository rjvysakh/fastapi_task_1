from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from fastapi_task_2.db.base import Base


class Document(Base):
    """
    Document class represents a document in the system.

    Attributes:
        id (int): The unique identifier for the document.
        document_id (str): The unique identifier for the document.
        document_url (str): The URL of the document.
        user_id (int): The ID of the user associated with the document.
        created_at (DateTime): The timestamp indicating when the document was created.
    """

    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, index=True, unique=True)
    document_url = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
