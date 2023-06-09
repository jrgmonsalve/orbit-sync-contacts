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
        
    def get_contacts_by_property(property_name: str, property_value: str) -> List[Contact]:
        api_key = settings.hubspot["api_key"]
        headers = {"Authorization": f"Bearer {api_key}"}
        url = f"https://api.hubapi.com/contacts/v1/lists/all/contacts/all?property={property_name}&property={property_value}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        contacts = []
        for contact in data['contacts']:
       
            email = contact.get('email', {}).get('value', '')
            firstname = contact.get('firstname', {}).get('value', '')
            lastname = contact.get('lastname', {}).get('value', '')
            phone = contact.get('phone', {}).get('value', '')
            website = contact.get('website', {}).get('value', '')
            contacts.append(Contact(
                email=email
                ,firstname=firstname
                ,lastname=lastname
                ,phone=phone
                ,website=website
                ))
        return contacts