from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from app import Base
import datetime

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }

class Event(Base,DictMixIn):
    __tablename__ = "Event"

    id = Column(Integer, primary_key=True, index=True)
    timestamp_insert = Column(String)
    timestamp_mod = Column(String)
    timestamp_event_start = Column(String)
    timestamp_event_end = Column(String)
    repetitive = Column(Integer)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    address = Column(Integer)
    lat = Column(Float)
    long = Column(Float)