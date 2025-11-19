from fastapi import FastAPI
from time_tracking.routers import tracking_routes

app = FastAPI()

app.include_router(tracking_routes.router)