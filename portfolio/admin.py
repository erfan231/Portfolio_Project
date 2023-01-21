from django.contrib import admin

from .models import Project, About, Contact, Socials_Info, Resume, Image, socialMedia_Images, skills, reviews,footer




# change header
admin.site.site_header = "Portfolio Admin"


# Register your models here.
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Socials_Info)
admin.site.register(Resume)
admin.site.register(Image)
admin.site.register(socialMedia_Images)
admin.site.register(skills)
admin.site.register(footer)
admin.site.register(reviews)


