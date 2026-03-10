from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Research(Base):

    __tablename__ = "research"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String)
    summary = Column(String)
    report = Column(String)