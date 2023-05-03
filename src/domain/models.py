from pydantic import BaseModel
from typing import Optional

class ContactRequest(BaseModel):
    email: str
    first_name: str
    last_name: str
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
