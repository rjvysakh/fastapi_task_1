from fastapi import APIRouter

router = APIRouter()


@router.get("/signup")
def signup() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
