from fastapi import APIRouter, Depends,  HTTPException
from time_tracking.database.db_connection import DatabaseConnection
from time_tracking.config import CONNECTION_STRING
from time_tracking.database import queries

import time_tracking.core.summary_analysis as summary_analysis

router = APIRouter(prefix="/summary", tags=["summary"])


db = DatabaseConnection(CONNECTION_STRING)

def get_db():
    return db


@router.get("/byemployee/{employee_id}", response_model=summary_analysis.SummaryReportForEmployee | dict)
def summary_by_employee(
    employee_id: int,
    db: DatabaseConnection = Depends(get_db)
):
    workshifts = queries.get_workshifts_by_employee(db=db, employee_id=employee_id)
    if not workshifts:
        return {"message": "Employee has no workshifts"}

    result = summary_analysis.analzye_workshifts_by_employee(employee_id, workshifts)

    return result


@router.get("/all_employees", response_model=summary_analysis.SummaryReportAll | dict)
def summary_all_employees(
    db: DatabaseConnection = Depends(get_db)
):
    workshifts = queries.get_all_workshifts(db=db)
    if not workshifts:
        return {"message": "There are no workshifts"}

    result = summary_analysis.analzye_all_workshifts(workshifts)

    return result

 
