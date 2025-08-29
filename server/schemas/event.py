from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from objectid import PyObjectId

class EventBase(BaseModel):
    name: str
    description: Optional[str] = None
    location: str
    date: datetime

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    date: Optional[datetime] = None

class EventPublic(EventBase):
    id: PyObjectId = Field(alias="_id")
    attendee_ids: List[str] = []

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}