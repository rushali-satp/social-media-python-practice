from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base

class User(Base):
    __tablename__ = "um_user"

    user_id = Column(Integer, primary_key=True, index=True)
    user_login_id = Column(String)
    user_official_name = Column(String)
    is_user = Column(String)
    created_on = Column(TIMESTAMP)
    password = Column(String)
    email_id = Column(String)
    mobile_no = Column(String)