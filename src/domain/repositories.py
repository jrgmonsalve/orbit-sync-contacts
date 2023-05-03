from src.domain.models import Contact, ContactRequest


class ContactRepository:
    def create(self, contact_request: ContactRequest) -> Contact:
        raise NotImplementedError