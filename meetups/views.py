from django.shortcuts import render, redirect
from . models import Meetup, Participant
from . forms import RegistrationForm

    

# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'showmeetups': False,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    
    
    try:
        selected_meetups = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':    
            # selected_meetups = Meetup.objects.get(slug=meetup_slug)            
            registration_form = RegistrationForm()            
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # participant = registration_form.save()
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetups.participants.add(participant)
                return redirect('confirm_registrations', meetup_slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
                'meetup_found':True,
                'meetup':selected_meetups,  
                'form': registration_form     
            })
    except Exception as exe:
        return render(request, 'meetups/meetup-details.html', {
        'meetup_found':False
              
    })
        
def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration_success.html',{
        'organizer_email' : meetup.organizer_email 
    })
        
        
    