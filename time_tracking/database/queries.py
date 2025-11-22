from time_tracking.database.db_connection import DatabaseConnection
from time_tracking.database.tables import Employee
from typing import Optional, List


def add_employee(db: DatabaseConnection, first_name: str, last_name: str, email: str) -> Employee:
    """Create a new employee."""
    with db.get_session() as session:
        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee


def delete_employee(db: DatabaseConnection, employee_id: int) -> bool:
    """Delete an employee by id. Returns True if deleted."""
    with db.get_session() as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            return False

        session.delete(employee)
        session.commit()
        return True


def update_employee(
    db: DatabaseConnection,
    employee_id: int,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    email: Optional[str] = None,
) -> Optional[Employee]:
    """Update an employee. Returns the updated employee or None."""
    with db.get_session() as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            return None

        if first_name is not None:
            employee.first_name = first_name
        if last_name is not None:
            employee.last_name = last_name
        if email is not None:
            employee.email = email

        session.commit()
        session.refresh(employee)
        return employee


def get_employee(db: DatabaseConnection, employee_id: int) -> Employee | None:
    """Return a single employee by ID."""
    with db.get_session() as session:
        employee = session.get(Employee, employee_id)
        return employee


def get_all_employees(db: DatabaseConnection) -> list[Employee]:
    """Return a list of all employees."""
    with db.get_session() as session:
        employees = session.query(Employee).all()
        return employees


from time_tracking.database.tables import WorkLog


def add_workshift(db, employee_id: int, start_time, end_time):
    with db.get_session() as session:

        overlap = session.query(WorkLog).filter(
            WorkLog.employee_id == employee_id,
            ((WorkLog.start_time < end_time) & (WorkLog.start_time > start_time)) | ((WorkLog.end_time < end_time) & (WorkLog.end_time > start_time))
        ).first()

        if overlap:
            raise ValueError("Workshift overlaps an existing shift.")
        
        log = WorkLog(
            employee_id=employee_id,
            start_time=start_time,
            end_time=end_time
        )
        session.add(log)
        session.commit()
        session.refresh(log)
        return log


def update_workshift(db, workshift_id: int, start_time=None, end_time=None):
    with db.get_session() as session:
        log = session.get(WorkLog, workshift_id)
        if not log:
            return None

        if start_time is not None:
            log.start_time = start_time
        if end_time is not None:
            log.end_time = end_time

        session.commit()
        session.refresh(log)
        return log


def delete_workshift(db, workshift_id: int):
    with db.get_session() as session:
        log = session.get(WorkLog, workshift_id)
        if not log:
            return False
        session.delete(log)
        session.commit()
        return True


def get_workshift(db, workshift_id: int):
    with db.get_session() as session:
        return session.get(WorkLog, workshift_id)


def get_all_workshifts(db):
    with db.get_session() as session:
        return session.query(WorkLog).all()


def get_workshifts_by_employee(db, employee_id: int) -> List[WorkLog]:
    with db.get_session() as session:
        return (
            session.query(WorkLog)
            .filter(WorkLog.employee_id == employee_id)
            .all()
        )