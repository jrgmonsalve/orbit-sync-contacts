from fastapi import FastAPI, HTTPException
from src.application.services import ContactService
from src.domain.models import Contact, ContactRequest, ContactSyncRequest
from src.infrastructure.hubspot_api import HubSpotContactRepository

app = FastAPI()
contact_service = ContactService(HubSpotContactRepository())

@app.post("/contacts", response_model=Contact, status_code=201, tags=["contacts"], summary="Create a contact in hubspot")
def create_contact(contact_request: ContactRequest):
    try:
        contact:Contact = contact_service.create_contact(contact_request)
        return contact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/contacts/sync", response_model=Contact, status_code=202, summary="Syncronice a contact from hubspot to clickup")
def sync_contact(contact_sync_request: ContactSyncRequest):
    pass