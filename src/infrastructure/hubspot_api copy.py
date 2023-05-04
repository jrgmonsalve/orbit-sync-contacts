from typing import List
import requests
from src.domain.models import Contact, ContactRequest

from src.domain.repositories import ContactRepository

from src.config import settings

class HubSpotContactRepository(ContactRepository):
    def create(self, contact_request: ContactRequest) -> Contact:
        url = "https://api.hubapi.com/crm/v3/objects/contacts?hapikey="+settings.hubspot["api_key"]
        headers = {"Content-Type": "application/json"}
        data = {
            "properties": [
                {"property": "email", "value": contact_request.email},
                {"property": "firstname", "value": contact_request.firstname},
                {"property": "lastname", "value": contact_request.lastname},
                {"property": "phone", "value": contact_request.phone},
                {"property": "website", "value": contact_request.website},
            ]
        }
        response = requests.post(url, headers=headers, json=data)
        print(response.json())
        if response.status_code == 200:
            return Contact(**response.json())
        else:
            raise Exception("Failed to create contact in HubSpot")
        
    def create_clickup_task(contact: Contact):
        token = settings.clickup["token"]
        list_id = settings.clickup["list_id"]
        url = f"https://api.clickup.com/api/v2/list/{list_id}/task"
        headers = {"Authorization": token}
        data = {
            "name": contact.firstname + " " + contact.lastname
            # TODO fill in the rest of the data
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()