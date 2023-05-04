from pydantic import BaseModel
from typing import Optional

from sqlalchemy import Column, Integer, String, JSON, DateTime
from database import Base
from datetime import datetime

class FilterContactsRequest(BaseModel):
    estado_clickup: str

class RequestLog(Base):
    __tablename__ = "request_logs"
    id = Column(Integer, primary_key=True, index=True)
    method = Column(String)
    url = Column(String)
    path = Column(String)
    headers = Column(JSON)
    body = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

class ContactRequest(BaseModel):
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str

class ContactSyncRequest(BaseModel):
    typeSync: str = "bulk" # bulk or onebyone

class Contact(BaseModel):
    id: int
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str
