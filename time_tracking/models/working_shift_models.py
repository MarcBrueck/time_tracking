from pydantic import BaseModel, EmailStr, model_validator
from typing import Optional
from datetime import datetime, timedelta


class WorkLogCreate(BaseModel):
    employee_id: int
    start_time: datetime
    end_time: datetime

    @model_validator(mode="after")
    def check_time_order(self):
        if self.end_time <= self.start_time:
            raise ValueError("end_time must be after start_time")
        
        duration = self.end_time - self.start_time
        if duration > timedelta(hours=16):
            raise ValueError("Working shifts cannot be longer than 16 hours")

        return self




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

    @property
    def work_shift_time(self)  -> timedelta:
        return self.end_time - self.start_time