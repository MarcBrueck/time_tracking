from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from time_tracking.database.db_connection import DatabaseConnection, CONNECTION_STRING
from time_tracking.database.tables import Employee
from time_tracking.database import queries
from time_tracking.models.simple_models import EmployeeCreate

router = APIRouter(prefix="/employees", tags=["employees"])


db = DatabaseConnection(CONNECTION_STRING)
db.create_tables()

def get_db():
    return db



@router.post("/add", response_model=str)
def create_employee(
    employee: EmployeeCreate,
    db: DatabaseConnection = Depends(get_db)
):
    created = queries.add_employee(
        db=db,
        first_name=employee.first_name,
        last_name=employee.last_name,
        email=employee.email
    )
    return f"Employee created with ID {created.id}"