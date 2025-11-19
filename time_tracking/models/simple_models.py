from pydantic import BaseModel, EmailStr

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr