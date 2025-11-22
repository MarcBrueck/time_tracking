from time_tracking.database.tables import WorkLog
from time_tracking.models.working_shift_models import WorkLogRead
from typing import List
from pydantic import BaseModel
from datetime import timedelta


class SummaryReportForEmployee(BaseModel):
    employee_id : int
    total_shifts: int
    total_work_hours: float


class SummaryReportAll(BaseModel):
    total_shifts: int
    total_work_hours: float


def analzye_workshifts_by_employee(employee_id: int, workshifts: List[WorkLog]) -> SummaryReportForEmployee:
    total_shifts = len(workshifts)
    total_time = timedelta()
    for workshift in workshifts:
        ws = WorkLogRead.model_validate(workshift)
        total_time += ws.work_shift_time

    total_work_hours = total_time.total_seconds() / 3600

    summary_report_for_employee = SummaryReportForEmployee(employee_id=employee_id, total_shifts=total_shifts, total_work_hours=total_work_hours)
    return summary_report_for_employee


def analzye_all_workshifts(workshifts: List[WorkLog]) -> SummaryReportAll:
    total_shifts = len(workshifts)
    total_time = timedelta()
    for workshift in workshifts:
        ws = WorkLogRead.model_validate(workshift)
        total_time += ws.work_shift_time

    total_work_hours = total_time.total_seconds() / 3600

    summary_report_all = SummaryReportAll(total_shifts=total_shifts, total_work_hours=total_work_hours)
    return summary_report_all