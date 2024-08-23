from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CVEBaseModel(BaseModel):
    cve_id: str
    published_date: datetime
    last_modified_date: datetime
    title: str
    description: str
    problem_types: Optional[str] = None

    class Config:
        orm_mode = True


class CVERecordCreate(CVEBaseModel):
    pass


class CVERecord(CVEBaseModel):
    id: int
