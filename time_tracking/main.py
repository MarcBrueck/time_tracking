from fastapi import FastAPI
from routers import employee_routes, working_shift_routes
from time_tracking.database.db_connection import DatabaseConnection
from time_tracking.config import CONNECTION_STRING

app = FastAPI()

db = DatabaseConnection(CONNECTION_STRING)
db.create_tables()

app.include_router(employee_routes.router)


app.include_router(working_shift_routes.router)
