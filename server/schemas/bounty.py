from pydantic import BaseModel, Field
from objectid import PyObjectId

class BountyCreate(BaseModel):
    title: str
    description: str
    prize: str
    sponsor_id: str

class BountyPublic(BountyCreate):
    id: PyObjectId = Field(alias="_id")
    is_claimed: bool = False

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}