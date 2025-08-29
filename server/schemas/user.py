from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from .objectid import PyObjectId

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    skills: List[str] = []
    interests: List[str] = []
    bio: Optional[str] = None

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    skills: Optional[List[str]] = None
    interests: Optional[List[str]] = None
    bio: Optional[str] = None

class UserPublic(UserBase):
    """Schema for public user data returned by the API."""
    id: PyObjectId = Field(alias="_id")

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}