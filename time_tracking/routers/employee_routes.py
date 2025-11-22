from fastapi import APIRouter, Depends,  HTTPException
from sqlalchemy.orm import Session
from time_tracking.database.db_connection import DatabaseConnection
from time_tracking.config import CONNECTION_STRING
from time_tracking.database import queries
from time_tracking.models.simple_models import EmployeeCreate, EmployeeUpdate, EmployeeRead

router = APIRouter(prefix="/employees", tags=["employees"])


db = DatabaseConnection(CONNECTION_STRING)

def get_db():
    return db


@router.post("/add", response_model=dict)
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
    return {
        "id": created.id,
        "message": "Employee created successfully"
    }



@router.put("/update/{employee_id}", response_model=dict)
def update_employee(
    employee_id: int,
    update_data: EmployeeUpdate,
    db: DatabaseConnection = Depends(get_db)
):
    updated = queries.update_employee(
        db=db,
        employee_id=employee_id,
        first_name=update_data.first_name,
        last_name=update_data.last_name,
        email=update_data.email
    )

    if updated is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {
        "id": employee_id,
        "message": "Employee updated successfully"
    }



@router.delete("/delete/{employee_id}", response_model=dict)
def delete_employee(
    employee_id: int,
    db: DatabaseConnection = Depends(get_db)
):
    deleted = queries.delete_employee(db=db, employee_id=employee_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {
        "id": employee_id,
        "message": "Employee deleted successfully"
    }


@router.get("/{employee_id}", response_model=EmployeeRead)
def get_employee(employee_id: int, db: DatabaseConnection = Depends(get_db)):
    employee = queries.get_employee(db=db, employee_id=employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.get("/", response_model=list[EmployeeRead])
def get_all_employees(db: DatabaseConnection = Depends(get_db)):
    employees = queries.get_all_employees(db=db)
    return employees