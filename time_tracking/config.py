from dotenv import load_dotenv
import os

load_dotenv()

# Here I decided to use sqlite, because it is the easiest to set up
# CONNECTION_STRING="sqlite:///time_tracking.db"

# For Postgres:
# CONNECTION_STRING = "postgresql://user:password@localhost:5432/mydb"

CONNECTION_STRING = os.getenv("CONNECTION_STRING", "sqlite:///time_tracking.db")