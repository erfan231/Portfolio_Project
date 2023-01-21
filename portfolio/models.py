from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, default="Erfan | Developer")
    name = models.CharField(max_length=200, default="Erfan Mahmoodi")
    about = models.TextField(max_length=5000)

    # this is a method that will return the title of the project
    # used for testing purposes
    def __str__(self):
        return self.about

class Image(models.Model):
    #field for svg file
    
    image = models.FileField(upload_to='images/background/')

    # this is a method that will return the title of the project
    # used for testing purposes
    def __str__(self):
        return self.image.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    link = models.URLField(max_length=2000, default="")
    image = models.ImageField(upload_to='images/projects/')

    # this is a method that will return the title of the project
    # used for testing purposes
    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    # this is a method that will return the title of the project
    # used for testing purposes
    def __str__(self):
        return self.name


class Resume(models.Model):
    resume = models.FileField(upload_to='resume/')

    # this is a method that will return the title of the project
    # used for testing purposes


class Socials_Info(models.Model):
    social_name = models.CharField(default='not provided', max_length=500)
    social_link = models.URLField(max_length=200, default="google.com")

    def __str__(self):
        return self.social_name




class socialMedia_Images(models.Model):
    socialImage = models.FileField(upload_to='images/socials/')
    # relational database to the Personal_Info model
    social_info = models.ForeignKey(Socials_Info, on_delete=models.CASCADE)

    # this is a method that will return the title of the project
    # used for testing purposes
    def __str__(self):
        return self.social_info.social_name



class skills(models.Model):
    skill = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/skills/')

    # this is a method that will return the title of the project
    # used for testing purposes
    def __str__(self):
        return self.skill


class footer(models.Model):
    footer = models.TextField(max_length=1000)

    # this is a method that will return the title of the project
    # used for testing purposes
    def __str__(self):
        return self.footer


class reviews(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/reviews/')

    # this is a method that will return the title of the project
    # used for testing purposes
    def __str__(self):
        return self.title