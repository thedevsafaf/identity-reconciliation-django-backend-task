from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Contact
from django.db.models import Q

@csrf_exempt
# Create your views here.
def identify(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        phoneNumber = data.get('phoneNumber')

        # Query the database to find contacts with matching email/phoneNumber
        matching_contacts = Contact.objects.filter(
            Q(email=email) | Q(phoneNumber=phoneNumber)
        )


        if matching_contacts.exists():
            primary_contact = matching_contacts.order_by('createdAt').first()
            secondary_contacts = matching_contacts.exclude(id=primary_contact.id)

            response_data = {
                "contact": {
                    "primaryContactId": primary_contact.id,
                    "emails": [primary_contact.email] + [contact.email for contact in secondary_contacts],
                    "phoneNumbers": [primary_contact.phoneNumber] + [contact.phoneNumber for contact in secondary_contacts],
                    "secondaryContactIds": [contact.id for contact in secondary_contacts]
                }
            }

        else:
            # we create a new primary contact if no matching contacts found
            new_contact = Contact.objects.create(
                phoneNumber=phoneNumber,
                email=email,
                linkPrecedence="primary"
            )

            response_data = {
                "contact": {
                    "primaryContactId": new_contact.id,
                    "emails": [new_contact.email],
                    "phoneNumbers": [new_contact.phoneNumber],
                    "secondaryContactIds": []
                }
            }

        return JsonResponse(response_data)   
    
# view for all contacts display

def view_contacts(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contacts/view_contacts.html', context)  

