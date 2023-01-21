from django.shortcuts import render, HttpResponse
from .models import Project, About, Contact, Resume, Image, socialMedia_Images, skills, footer, reviews
from .forms import ContactForm
from django.contrib import messages
from .scripts import SendMessage

# Create your views here.


def index(request):
    #return HttpResponse("Hi!")
    forms = ContactForm()

    try:
        # query all the projects
        project_query = Project.objects.all()
        # query the last about object
        about_query = About.objects.last()
        # query the last image object
        image_query = Image.objects.last()

        socials_query = socialMedia_Images.objects.all()
        footer_query = footer.objects.last()


        projects = {"projects": project_query,
                    "about": about_query,
                    "image": image_query,
                    "socials": socials_query,
                    "form": forms,
                    "footer": footer_query
                    }

    except Project.DoesNotExist:
        query = None
        projects = {"projects": query}
    
    if request.method == 'POST':
            forms = ContactForm(request.POST)
            if forms.is_valid():
                #forms.save()
                # sent msg Discord API
                # get the value of the name input
                name = forms.cleaned_data['name']
                # get the value of the email input
                email = forms.cleaned_data['email']
                # get the value of the message input
                message = forms.cleaned_data['message']
                # send the message to discord
                SendMessage(name, email, message)
                #save contact form to db
                form = Contact(name=name, email=email, message=message)
                form.save()
                messages.success(request, 'Details succesfully saved.')
                print(name, email, message)
                return render(request, 'portfolio/index.html',projects)
            else:
                messages.error(request, 'Complete captcha and try again.')
                return render(request, 'portfolio/index.html',projects)


    return render(request, 'portfolio/index.html',projects)


def resume(request):
    about_query = About.objects.last()
    skills_query = skills.objects.all()
    footer_query = footer.objects.last()
    resume_query = Resume.objects.last()
    socials_query = socialMedia_Images.objects.all()
    review_query = reviews.objects.all()

    projects = {
                "about": about_query,
                "skills": skills_query,
                "footer": footer_query,
                "resume": resume_query,
                "socials": socials_query,
                "reviews": review_query

                }
    return render(request, 'portfolio/resume.html', projects)


def review(request):
    review_query = reviews.objects.all()
    about_query = About.objects.last()
    social_query = socialMedia_Images.objects.all()

    objects = {
                "reviews": review_query,
                "about": about_query,
                "socials": social_query,
                }

    return render(request, 'portfolio/reviews.html', objects)



def test(request):
    review_query = reviews.objects.all()

    objects = {
                "reviews": review_query
    }
    return render(request, 'portfolio/test.html', objects)