from dotenv import load_dotenv
import os

# Load .env before importing anything that depends on env vars
load_dotenv()

CONNECTION_STRING = os.getenv("CONNECTION_STRING", "sqlite:///time_tracking.db")