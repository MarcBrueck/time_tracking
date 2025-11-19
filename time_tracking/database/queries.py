from time_tracking.database.db_connection import DatabaseConnection
from time_tracking.database.tables import Employee
from typing import Optional


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
