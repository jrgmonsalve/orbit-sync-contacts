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
                {"property": "firstname", "value": contact_request.first_name},
                {"property": "lastname", "value": contact_request.last_name},
                {"property": "phone", "value": contact_request.phone},
                {"property": "website", "value": contact_request.website},
            ]
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return Contact(**response.json())
        else:
            raise Exception("Failed to create contact in HubSpot")