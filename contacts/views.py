from django.shortcuts import render,redirect
from .models import Contacts
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def contact(request):
    if request.method=="POST":
        listing_id=request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

    #check if user is authenticated
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted=Contacts.objects.all().filter(listing_id=listing_id,user_id=user_id)
        if has_contacted:
            messages.error(request,'You have already made and Enquiry for this listing, Our Realtor will get in touch with you')
            return redirect('/listings/'+listing_id)
        else:
            messages.success(request, 'your request has been submitted our realtor will get in touch with you')
        return redirect('/listings/'+listing_id)

        contact = Contacts(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        
         #send Mail
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for' + listing + '. Sign to the admin for more info',
            'kuppalabharathkumar.py@gmail.com',
            [realtor_email,'bharathkuppala309@gmail.com'],
            fail_silently=False
        )
        messages.success(request,'your request has been submitted our realtor will get in touch with you')
        return redirect('/listings/'+listing_id)

    contact = Contacts(listing=listing, listing_id=listing_id, name=name,
                       email=email, phone=phone, message=message, user_id=user_id)
    contact.save()

    send_mail(
        'Property Listing Inquiry',
        'There has been an inquiry for' + listing + '. Sign to the admin for more info',
        'kuppalabharathkumar.py@gmail.com',
        [realtor_email, 'bharathkuppala309@gmail.com'],
        fail_silently=False)
    messages.success(request, 'your request has been submitted a realtor will get in touch with you')
    return redirect('/listings/'+listing_id)


