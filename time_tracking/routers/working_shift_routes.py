from fastapi import APIRouter, Depends, HTTPException
from time_tracking.database.db_connection import DatabaseConnection
from time_tracking.database import queries
from time_tracking.config import CONNECTION_STRING
from time_tracking.models.working_shift_models import (
    WorkLogCreate,
    WorkLogUpdate,
    WorkLogRead
)

router = APIRouter(prefix="/workshifts", tags=["workshifts"])

db = DatabaseConnection(CONNECTION_STRING)

def get_db():
    return db



@router.post("/add", response_model=WorkLogRead)
def add_workshift(
    workshift: WorkLogCreate,
    db: DatabaseConnection = Depends(get_db)
):
    created = queries.add_workshift(
        db=db,
        employee_id=workshift.employee_id,
        start_time=workshift.start_time,
        end_time=workshift.end_time
    )
    return created



@router.put("/update/{workshift_id}", response_model=WorkLogRead)
def update_workshift(
    workshift_id: int,
    update_data: WorkLogUpdate,
    db: DatabaseConnection = Depends(get_db)
):
    updated = queries.update_workshift(
        db=db,
        workshift_id=workshift_id,
        start_time=update_data.start_time,
        end_time=update_data.end_time
    )

    if updated is None:
        raise HTTPException(status_code=404, detail="Work log not found")

    return updated



@router.delete("/delete/{workshift_id}", response_model=dict)
def delete_workshift(
    workshift_id: int,
    db: DatabaseConnection = Depends(get_db)
):
    deleted = queries.delete_workshift(db=db, workshift_id=workshift_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Work log not found")

    return {
        "id": workshift_id,
        "message": "Work log deleted successfully"
    }



@router.get("/{workshift_id}", response_model=WorkLogRead)
def get_workshift(
    workshift_id: int,
    db: DatabaseConnection = Depends(get_db)
):
    log = queries.get_workshift(db=db, workshift_id=workshift_id)

    if not log:
        raise HTTPException(status_code=404, detail="Work log not found")

    return log



@router.get("/", response_model=list[WorkLogRead])
def get_all_workshifts(
    db: DatabaseConnection = Depends(get_db)
):
    logs = queries.get_all_workshifts(db=db)
    return logs



@router.get("/employee/{employee_id}", response_model=list[WorkLogRead])
def get_workshifts_by_employee(
    employee_id: int,
    db: DatabaseConnection = Depends(get_db)
):
    logs = queries.get_workshifts_by_employee(db=db, employee_id=employee_id)
    return logs