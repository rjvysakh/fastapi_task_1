from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

from fastapi_task_2.db.crud import create_user, get_user_by_username
from fastapi_task_2.db.database import SessionLocal
from fastapi_task_2.services.auth import create_access_token, verify_password

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserRegistration(BaseModel):
    """
    Registration Model for formData.
    
    :yield: UserRegistration Model
    """
    username: str
    password: str


def get_db():
    """
    Get a SQLAlchemy database session.

    :yield: Database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from fastapi import Body


@router.post("/login")
async def login_for_access_token(
    user_data: UserRegistration = Body(...), db: Session = Depends(get_db),
):
    """
    Endpoint for user login and generating an access token.

    :param user_data: Data for user login (username and password) in the request body
    :param db: SQLAlchemy database session
    :return: Dictionary containing access token and token type
    """
    user = get_user_by_username(db, username=user_data.username)
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.id},
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register")
async def register_user(user_data: UserRegistration, db: Session = Depends(get_db)):
    """
    Endpoint for registering a new user.

    :param user_data: Data for the new user (username and password)
    :param db: SQLAlchemy database session
    :return: Created user details
    """
    user = get_user_by_username(db, username=user_data.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="Username already registered",
        )
    hashed_password = pwd_context.hash(user_data.password)
    return create_user(db, username=user_data.username, hashed_password=hashed_password)
