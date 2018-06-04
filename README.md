# maintenance-tracker-api
[![Build Status](https://travis-ci.org/lytes20/maintenance-tracker-api.svg?branch=master)](https://travis-ci.org/lytes20/maintenance-tracker-api)
[![Coverage Status](https://coveralls.io/repos/github/lytes20/maintenance-tracker-api/badge.svg)](https://coveralls.io/github/lytes20/maintenance-tracker-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/017a6ef86505f7dc755a/maintainability)](https://codeclimate.com/github/lytes20/maintenance-tracker-api/maintainability)

## About
Maintenance Tracker App is an application that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.

The API for a maintenance tracker application allows users and admins to have the mentioned functionality above
## Features
- Get all the requests for a logged in user
- Get a request for a logged in user
- Create a request.
- Modify a request
- Register a user
- Login a user
## Tools Used
[Flask](http://flask.pocoo.org/) - web microframework for Python
[Virtual environment](https://virtualenv.pypa.io/en/stable/) - tool used to create isolated python environments
[pip](https://pip.pypa.io/en/stable/) - tool used used to install python messages
[git](https://git-scm.com/) - free open source distributed version control system
## Requirements
[Python](https://www.python.org/) 3.x.x+
## Run (Use) on your local machine
First clone the repository
```sh
   $ git clone https://github.com/lytes20/maintenance-tracker-api.git
   ```
   Head over to the cloned directory, create a virtual environment, use pip to install the requirements, the run the app
   ```sh
    $ cd maintenance-tracker-api
    $ virtualenv venv
    $ source venv/Scripts/activate
    $ pip install -r requirements.txt
    $ python run.py
```
#### Endpoints to create a user account and login into the application
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | v1/user/register | True | Create an account
POST | v1/user/login | True | Login a user

#### Endpoints to create, read and update user requests
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | v1/users/requests | True | Create a request
GET | v1/users/requests | False | Fetch requests for a logged in user
GET | v1/users/requests/requestid | False | Fetch a request for a logged in user
PUT | v1/users/requests/requestid | False | Update a request for a logged in user

## Authors
[Bamuleseyo Gideon](https://github.com/lytes20)
