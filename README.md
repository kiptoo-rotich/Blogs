#  Blog

#### Author: [Kiptoo-Rotich](https://github.com/Kiptoo-Rotich)


## Description
The application will allows a user to post a blogs of various fields and also displays random quotes with their authors.

As a user of the web application you will be able to:

1. Sign up and log in
2. View random quotes
3. Post blogs

## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='awwards'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations news
python3.8 manage.py sqlmigrate news 0001
python3.8 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:5000](http://127.0.0.1:5000/)



## Testing the Application
`python manage.py test insta`
        
## Built With

* [Python3.8](https://docs.python.org/3/)
* Postgresql 
* Boostrap
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)