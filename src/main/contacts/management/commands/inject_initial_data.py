from django.core.management.base import BaseCommand
from contacts.models import Contact

class Command(BaseCommand):
    help = 'Populate initial data for the Contact model'

    def handle(self, *args, **options):
        Contact.objects.create(
            phoneNumber="123456",
            email="lorraine@hillvalley.edu",
            linkPrecedence="primary"
        )
        Contact.objects.create(
            phoneNumber="123456",
            email="mcfly@hillvalley.edu",
            linkedId=1,
            linkPrecedence="secondary"
        )
        self.stdout.write(self.style.SUCCESS('Initial data populated successfully'))