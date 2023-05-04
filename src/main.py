from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from src.application.services import ContactService
from src.core.middleware import middleware
from src.domain.models import Contact, ContactRequest, ContactSyncRequest, FilterContactsRequest
from src.infrastructure.hubspot_api import HubSpotContactRepository

app = FastAPI()
hubspot_contact_service = ContactService(HubSpotContactRepository())
clickup_task_service = TaskService(ClickUpTaskRepository())

app.middleware("http")(middleware)

@app.post("/contacts", response_model=Contact, status_code=201, tags=["contacts"], summary="Create a contact in hubspot")
def create_contact(contact_request: ContactRequest):
    try:
        contact:Contact = hubspot_contact_service.create_contact(contact_request)
        return contact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/contacts/sync", response_model=Contact, status_code=202, summary="Syncronice a contact from hubspot to clickup")
async def sync_contacts(background_tasks: BackgroundTasks, request: FilterContactsRequest):
    """Endpoint that syncs contacts from HubSpot to ClickUp"""
    # 1. Retrieve contacts from HubSpot with the specified flag
    hubspot_contacts = await hubspot_contact_service.get_contacts_by_property("estado_clickup",request.estado_clickup)
    # 2. Create a ClickUp task for each contact in the background
    for contact in hubspot_contacts:
        background_tasks.add_task(clickup_task_service.create_task, contact)
    return {"message": f"Syncing {len(hubspot_contacts)} contacts in the background"}