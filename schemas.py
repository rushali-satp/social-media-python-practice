from datetime import datetime
from pydantic import BaseModel

class UserResponse(BaseModel):
    user_id: int
    user_login_id: str
    user_official_name: str
    is_user: str
    created_on: datetime
    email_id: str
    mobile_no: str

    class Config:
        from_attributes = True

class ContactRequest(BaseModel):
    contact_number: str