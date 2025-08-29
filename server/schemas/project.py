from pydantic import BaseModel, Field
from typing import List, Optional
from .objectid import PyObjectId

class ProjectBase(BaseModel):
    name: str
    description: str
    required_skills: List[str] = []

class ProjectCreate(ProjectBase):
    event_id: str

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    required_skills: Optional[List[str]] = None

class ProjectPublic(ProjectBase):
    id: PyObjectId = Field(alias="_id")
    owner_id: str
    team_member_ids: List[str] = []
    event_id: str

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}