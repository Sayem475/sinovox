from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    websitetitles_data = WebsiteTitles.objects.get_or_create_singleton()
    hero_data = HeroSection.objects.get_or_create_singleton()
    about_data = AboutSection.objects.get_or_create_singleton()

    service_summary_data = ServiceSummarySection.objects.all()
    counter_data = CounterSection.objects.all()
    approach_data = ApproachSection.objects.all()
    commitment_data = CommitmentSection.objects.all()
    allservice_data = AllServicesSection.objects.all()
    whychoose_data = WhyChooseUsSection.objects.all()

    contact_data = Contact.objects.get_or_create_singleton()
    social_data = SocialLinks.objects.get_or_create_singleton()
    websitesetting_data = WebsiteSettings.objects.get_or_create_singleton()
    pricing_data = PricingSection.objects.get_or_create_singleton()
    context ={
        'hero_data':hero_data,
        'about_data':about_data,
        'service_summary_data':service_summary_data,
        'counter_data':counter_data,
        'approach_data':approach_data,
        'commitment_data':commitment_data,
        'allservice_data':allservice_data,
        'hero_dwhychoose_dataata':whychoose_data,
        'contact_data':contact_data,
        'social_data':social_data,
        'websitesetting_data':websitesetting_data,
        'pricing_data':pricing_data,
    }
    return render(request, 'pages/home.html', context)