from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class WorkLogCreate(BaseModel):
    employee_id: int
    start_time: datetime
    end_time: datetime


class WorkLogUpdate(BaseModel):
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class WorkLogRead(BaseModel):
    id: int
    employee_id: int
    start_time: datetime
    end_time: datetime
    created_at: datetime

    class Config:
        from_attributes = True