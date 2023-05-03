from src.domain.models import Contact, ContactRequest
from src.domain.repositories import ContactRepository


class ContactService:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository
    
    def create_contact(self, contact_request: ContactRequest) -> Contact:
        return self.contact_repository.create(contact_request)