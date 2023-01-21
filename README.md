
# Portfolio

A simpple portfolio project build with Django. The portfolio consists of 3 main indexes but can be
extend if you wish to do so.

The website is dynamic so the contents of the website can be updated, added or deleted from the admin panel.

Currently the following can be updated, added, deleted from the admin panel:

- *Profile Picture*
- *Projects*
- *About Me*
- *Contact Info*
- *Social Info*
- *Resume*
- *Images*
- *Social media images*
- *Skills*
- *Reviews*
- *Footer*






## Installation

Install the project

```git
  git clone https://github.com/erfan231/Portfolio_Project.git
  cd myportfolio
  pip install -r requirements.txt
```
    
## Set-up
```bash
python manage.py makemigrations portfolio
python manage.py migrate
python manage.py createsuperuser

```

# Registering to Google reCAPTCHA Admin Console:
https://www.geeksforgeeks.org/how-to-add-google-recaptcha-to-django-forms/
## Run Locally



Go to the project directory

```bash
 python manage.py runserver 5000
```
## Demo

https://erfan.engineer


## Environment Variables

To run this project, you will need to add the following environment variables.

`SECRET_KEY`

`RECAPTCHA_PUBLIC_KEY`

`RECAPTCHA_PRIVATE_KEY`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`

`DB_PORT`

`DISCORD_WEBHOOK`

`ANOTHER_API_KEY`


## Tech Stack

**Client:** Django, Python3, jazzmin, bootstrap, fontawesome-free

**Database:** Postgresql

**server** Digitalocean


## Authors

- [@Erfan Mahmoodi](https://www.github.com/erfan231)

