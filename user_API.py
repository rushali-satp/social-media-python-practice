from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserResponse, ContactRequest

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/by-contact", response_model=UserResponse)
def get_user_by_contact(
    request: ContactRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.mobile_no == request.contact_number
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user