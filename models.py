from sqlalchemy import Column, Integer, String, DateTime
from db import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    posted = Column(DateTime, default=datetime.utcnow)
