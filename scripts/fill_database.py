import random
import requests
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

BASE_URL = "http://localhost:8000"   # adjust if needed


# -------------------------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------------------------

def create_employee():
    """Create a fake employee via the API."""
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name}.{last_name}.{random.randint(1000,9999)}@example.com".lower()

    response = requests.post(
        f"{BASE_URL}/employees/add",
        json={
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
    )
    if response.status_code != 200:
        print("Failed to create employee:", response.text)
        return None

    # response is: "Employee created with ID X"
    employee_id = int(response.text.split()[-1])
    return employee_id


def create_random_workshift(employee_id: int):
    """Create a random *non-overlapping* work shift for an employee."""
    # random day in the last 30 days
    day = fake.date_between(start_date='-30d', end_date='today')

    start_hour = random.randint(6, 14)
    duration_hours = random.randint(4, 9)

    start = datetime.combine(day, datetime.min.time()) + timedelta(hours=start_hour)
    end = start + timedelta(hours=duration_hours)

    response = requests.post(
        f"{BASE_URL}/workshifts/add",
        json={
            "employee_id": employee_id,
            "start_time": start.isoformat(),
            "end_time": end.isoformat()
        }
    )

    if response.status_code != 200:
        print("Failed to create shift:", response.text)
    else:
        print(f"  → shift: {start} → {end}")


# -------------------------------------------------------------------------------------
# Main Seeder
# -------------------------------------------------------------------------------------

def seed_demo_data(
    employee_count: int = 50,
    min_shifts: int = 5,
    max_shifts: int = 10
):
    print("🚀 Starting seed script...")

    created_employees = []

    # ---- CREATE EMPLOYEES ----
    print(f"\nCreating {employee_count} employees...")
    for _ in range(employee_count):
        emp_id = create_employee()
        if emp_id:
            created_employees.append(emp_id)
            print(f"Created employee {emp_id}")

    # ---- CREATE WORK SHIFTS FOR EACH EMPLOYEE ----
    print(f"\nCreating work shifts...")
    for emp_id in created_employees:
        shift_count = random.randint(min_shifts, max_shifts)
        print(f"\nEmployee {emp_id} → generating {shift_count} shifts...")
        for _ in range(shift_count):
            create_random_workshift(emp_id)

    print("\n🎉 Seeding complete!")


if __name__ == "__main__":
    seed_demo_data()
