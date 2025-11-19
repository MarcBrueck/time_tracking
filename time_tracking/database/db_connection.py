from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from time_tracking.database.tables import Base

CONNECTION_STRING = "sqlite:///time_tracking.db"
# For Postgres:
# DATABASE_URL = "postgresql://user:password@localhost:5432/mydb"




class DatabaseConnection:
    def __init__(self, connection_string):
        self.conn_string = connection_string
        self.engine = create_engine(self.conn_string, echo=False)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)
        
    def get_session(self):
        return self.SessionLocal()
        
    def drop_tables(self):
        Base.metadata.drop_all(bind=self.engine)


