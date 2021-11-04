from django.urls import path
from . import views

urlpatterns = [
    # path('meetups/', views.index, name='all-meetups'), # domain.com/meetups
    # path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name= 'confirm_registrations'),
    # path('meetups/<slug:meetup_slug>', views.meetup_details, name = 'meetup_details') # domain.com/meetups/<dynamic-pth-segment>
    path('', views.index, name='all-meetups'), # domain.com/meetups
    path('<slug:meetup_slug>/success', views.confirm_registration, name= 'confirm_registrations'),
    path('<slug:meetup_slug>', views.meetup_details, name = 'meetup_details') # domain.com/meetups/<dynamic-pth-segment>
    
]
