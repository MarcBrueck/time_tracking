import pytest
from datetime import datetime, timezone

from time_tracking.core.summary_analysis import (
    analzye_workshifts_by_employee,
    SummaryReportForEmployee,
    WorkLog,
)

# PYTHONPATH=. pytest

def test_analyze_workshifts_by_employee():
    employee_id = 1

    workshifts = [
        WorkLog(
            id=1,
            employee_id=employee_id,
            start_time=datetime(2024, 1, 1, 8, 0, tzinfo=timezone.utc),
            end_time=datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc),
            created_at=datetime.now(timezone.utc)
        ),
        WorkLog(
            id=2,
            employee_id=employee_id,
            start_time=datetime(2024, 1, 2, 9, 0, tzinfo=timezone.utc),
            end_time=datetime(2024, 1, 2, 17, 0, tzinfo=timezone.utc),
            created_at=datetime.now(timezone.utc)
        ),
    ]

    # Expected: 4 hours + 8 hours = 12
    expected_hours = 12.0
    # expected_hours = 15.0

    result = analzye_workshifts_by_employee(employee_id, workshifts)

    assert isinstance(result, SummaryReportForEmployee)
    assert result.employee_id == employee_id
    assert result.total_shifts == 2
    assert pytest.approx(result.total_work_hours, 0.0001) == expected_hours