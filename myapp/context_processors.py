from .models import *

def website_settings_context(request):
    try:
        web_setting_data = WebsiteSettings.objects.latest('id')
    except WebsiteSettings.DoesNotExist:
        web_setting_data = None
    return {'web_setting_data': web_setting_data}

def social_links_context(request):
    try:
        social_links = SocialLinks.objects.latest('id')
    except Footer.DoesNotExist:
        social_links = None

    return {'social_links': social_links}


def contact_data_context(request):
    try:
        contact_data = Contact.objects.latest('id')
    except Footer.DoesNotExist:
        contact_data = None

    return {'contact_data': contact_data}
