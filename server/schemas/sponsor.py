from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from objectid import PyObjectId

class SponsorCreate(BaseModel):
    name: str
    website: HttpUrl
    logo_url: Optional[HttpUrl] = None
    tier: str

class SponsorPublic(SponsorCreate):
    id: PyObjectId = Field(alias="_id")

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}