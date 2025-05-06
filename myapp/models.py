from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.utils import timezone

# ALL TITLE IN WEBSITE 
class UniqueWebTitlesManager(models.Manager):
    def get_or_create_singleton(self):
        webtitles, created = self.get_or_create(pk=1)
        return webtitles

class WebsiteTitles(models.Model):
    en_about_title = models.CharField(max_length=1000,blank=True, null=True)
    en_about_short_description = models.TextField(max_length=1000,blank=True, null=True)
    en_summary_service_title = models.CharField(max_length=1000,blank=True, null=True)
    en_summary_service_short_discription = models.TextField(max_length=1000,blank=True, null=True)
    en_approach_title = models.CharField(max_length=1000,blank=True, null=True)
    en_approach_short_discription = models.TextField(max_length=1000,blank=True, null=True)
    en_all_service_title = models.CharField(max_length=1000,blank=True, null=True)
    en_all_service_discription = models.TextField(max_length=1000,blank=True, null=True)
    en_packages_title = models.CharField(max_length=1000,blank=True, null=True)
    en_packages_short_description = models.TextField(max_length=1000,blank=True, null=True)
    en_whychooseus_title = models.CharField(max_length=1000,blank=True, null=True)
    en_whychooseus_short_description = models.TextField(max_length=1000,blank=True, null=True)
    en_contact_title = models.CharField(max_length=1000,blank=True, null=True)
    en_contact_short_description = models.TextField(max_length=1000,blank=True, null=True)

    ch_about_title = models.CharField(max_length=1000,blank=True, null=True)
    ch_about_short_description = models.TextField(max_length=1000,blank=True, null=True)
    ch_summary_service_title = models.CharField(max_length=1000,blank=True, null=True)
    ch_summary_service_short_discription = models.TextField(max_length=1000,blank=True, null=True)
    ch_approach_title = models.CharField(max_length=1000,blank=True, null=True)
    ch_approach_short_discription = models.TextField(max_length=1000,blank=True, null=True)
    ch_all_service_title = models.CharField(max_length=1000,blank=True, null=True)
    ch_all_service_discription = models.TextField(max_length=1000,blank=True, null=True)
    ch_packages_title = models.CharField(max_length=1000,blank=True, null=True)
    ch_packages_short_description = models.TextField(max_length=1000,blank=True, null=True)
    ch_whychooseus_title = models.CharField(max_length=1000,blank=True, null=True)
    ch_whychooseus_short_description = models.TextField(max_length=1000,blank=True, null=True)
    ch_contact_title = models.CharField(max_length=1000,blank=True, null=True)
    ch_contact_short_description = models.TextField(max_length=1000,blank=True, null=True)

    objects = UniqueWebTitlesManager()
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = '01. Website Section Titles'
        verbose_name_plural = '01. Website Section Titles'


    def __str__(self):
        return f"Website All Section Titles and Short Descriptions"

# HERO SECTION 
class UniqueHeroSectionManager(models.Manager):
    def get_or_create_singleton(self):
        herosection, created = self.get_or_create(pk=1)
        return herosection

class HeroSection(models.Model):
    en_title = models.CharField(max_length=255)
    en_short_description = models.TextField(max_length=500)
    en_banner_image = models.ImageField(upload_to='banner/')

    ch_title = models.CharField(max_length=255,blank=True, null=True)
    ch_short_description = models.TextField(max_length=500,blank=True, null=True)
    ch_banner_image = models.ImageField(upload_to='banner/',blank=True, null=True)

    objects = UniqueHeroSectionManager()
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '02. Hero Section'
        verbose_name_plural = '02. Hero Section'
        
    def __str__(self):
        return f"Hero Section"

# ABOUT SECTION 
class UniqueAboutSectionManager(models.Manager):
    def get_or_create_singleton(self):
        aboutsection, created = self.get_or_create(pk=1)
        return aboutsection

class AboutSection(models.Model):
    en_title = models.CharField(max_length=255)
    en_short_description = models.TextField(max_length=1000)
    en_banner_image = models.ImageField(upload_to='banner/')

    ch_title = models.CharField(max_length=255,blank=True, null=True)
    ch_short_description = models.TextField(max_length=1000,blank=True, null=True)
    ch_banner_image = models.ImageField(upload_to='banner/',blank=True, null=True)

    objects = UniqueAboutSectionManager()
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '03. About Section'
        verbose_name_plural = '03. About Section'
        
    def __str__(self):
        return f"About Section"

# SERVICE SUMMARY SECTION 
class ServiceSummarySection(models.Model):
    en_service_summary_title = models.CharField(max_length=255)
    en_short_description = models.TextField(max_length=1000)

    ch_service_summary_title = models.CharField(max_length=255,blank=True, null=True)
    ch_short_description = models.TextField(max_length=1000,blank=True, null=True)

    class Meta:
        verbose_name = '04. Service Summary Section'
        verbose_name_plural = '04. Service Summary Section'
        
    def __str__(self):
        return self.service_summary_title

# COUNTER SECTION 
class CounterSection(models.Model):
    en_value = models.CharField(max_length=255,blank=True, null=True)
    en_title = models.CharField(max_length=500,blank=True, null=True)

    ch_value = models.CharField(max_length=255,blank=True, null=True)
    ch_title = models.CharField(max_length=500,blank=True, null=True)

    class Meta:
        verbose_name = '05. Counter Section'
        verbose_name_plural = '05. Counter Section'
        
    def __str__(self):
        return self.title

# OUR APPROACH 
class ApproachSection(models.Model):
    en_title = models.CharField(max_length=255,)
    en_description = models.TextField(max_length=1000,)

    ch_title = models.CharField(max_length=255,)
    ch_description = models.TextField(max_length=1000,)


    class Meta:
        verbose_name = '06. Our Approach Section'
        verbose_name_plural = '06. Our Approach Section'
        
    def __str__(self):
        return self.title

# OUR COMMITMENT       
class UniqueCommitmentSectionManager(models.Manager):
    def get_or_create_singleton(self):
        commitmentsection, created = self.get_or_create(pk=1)
        return commitmentsection

class CommitmentSection(models.Model):
    en_title = models.CharField(max_length=255,blank=True, null=True)
    en_short_description = models.TextField(max_length=1000,blank=True, null=True)
    en_banner_image = models.ImageField(upload_to='banner/',blank=True, null=True)

    ch_title = models.CharField(max_length=255,blank=True, null=True)
    ch_short_description = models.TextField(max_length=1000,blank=True, null=True)
    ch_banner_image = models.ImageField(upload_to='banner/',blank=True, null=True)

    objects = UniqueCommitmentSectionManager()
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '07. Our Commitment Section'
        verbose_name_plural = '07. Our Commitment Section'
        
    def __str__(self):
        return f"Our Commitment Section"

# ALL SERVICES SECTION       
class AllServicesSection(models.Model):
    en_title = models.CharField(max_length=255)
    en_short_description = models.TextField(max_length=500)

    ch_title = models.CharField(max_length=255)
    ch_short_description = models.TextField(max_length=500)

    class Meta:
        verbose_name = '08. All Services Section'
        verbose_name_plural = '08. All Services Section'
        
    def __str__(self):
        return self.title

# WHY CHOOSE US SECTION       
class WhyChooseUsSection(models.Model):
    en_title = models.CharField(max_length=255)
    en_short_description = models.TextField(max_length=500)

    ch_title = models.CharField(max_length=255)
    ch_short_description = models.TextField(max_length=500)

    class Meta:
        verbose_name = '09. Why Choose Us'
        verbose_name_plural = '09. Why Choose Us'
        
    def __str__(self):
        return self.title

# ADDRESS  
class UniqueContactManager(models.Manager):
    def get_or_create_singleton(self):
        contact_data, created = self.get_or_create(pk=1)
        return contact_data

class Contact(models.Model):
    en_address = models.TextField(max_length=1000,blank=True, null=True)
    en_email = models.CharField(max_length=50,blank=True, null=True)
    en_phone = models.CharField(max_length=50,blank=True, null=True)

    ch_address = models.TextField(max_length=1000,blank=True, null=True)
    ch_email = models.CharField(max_length=50,blank=True, null=True)
    ch_phone = models.CharField(max_length=50,blank=True, null=True)

    objects = UniqueContactManager()
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '10. Contact Details'
        verbose_name_plural = '10. Contact Details'

    def __str__(self):
        return 'Contact Details'

# UNIQUE 
class UniqueSocialLinksManager(models.Manager):
    def get_or_create_singleton(self):
        social_links, created = self.get_or_create(pk=1)
        return social_links

class SocialLinks(models.Model):
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    objects = UniqueSocialLinksManager()
    def save(self, *args, **kwargs):
        # Ensure only one instance is allowed
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '11. Social Links'
        verbose_name_plural = '11. Social Links'

    def __str__(self):
        return "Social Links"

# UNIQUE 
class UniqueWebsiteSettingsManager(models.Manager):
    def get_or_create_singleton(self):
        websiteSettings, created = self.get_or_create(pk=1)
        return websiteSettings

class WebsiteSettings(models.Model):
    favicon_icon = models.ImageField(upload_to='favicon_icons/',blank=True,null=True)
    website_logo = models.ImageField(upload_to='logo/',blank=True,null=True)
    service_section_background_image = models.ImageField(upload_to='service_background_image/',blank=True,null=True)
    en_website_title = models.CharField(max_length=255,blank=True, null=True)
    en_website_nav_title=models.CharField(max_length=255,blank=True,null=True)

    ch_website_title = models.CharField(max_length=255,blank=True, null=True)
    ch_website_nav_title=models.CharField(max_length=255,blank=True,null=True)

    objects = UniqueWebsiteSettingsManager()
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '12. Website Settings'
        verbose_name_plural = '12. Website Settings'

    def __str__(self):
        return self.website_title

# OUR PRICING       
class UniquePricingSectionManager(models.Manager):
    def get_or_create_singleton(self):
        pricingsection, created = self.get_or_create(pk=1)
        return pricingsection

class PricingSection(models.Model):
    en_currency_title = models.CharField(max_length=255,blank=True, null=True)
    en_short_description = models.TextField(max_length=1000,blank=True, null=True)

    ch_currency_title = models.CharField(max_length=255,blank=True, null=True)
    ch_short_description = models.TextField(max_length=1000,blank=True, null=True)

    objects = UniquePricingSectionManager()
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '13. Pricing Section'
        verbose_name_plural = '13. Pricing Section'
        
    def __str__(self):
        return f"Pricing Section"

