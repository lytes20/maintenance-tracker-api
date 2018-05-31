# maintenance-tracker-api
## About
This is an API for a maintenance tracker application that allows users to make maintenance or repair requests and monitor them
## Features
- Get all the requests for a logged in user
- Get a request for a logged in user
- Create a request.
- Modify a request
- Register a user
- Login a user
## Tools Used
[Flask](http://flask.pocoo.org/) - web microframework for Python
## Requirements
Python 3.x.x+
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
GET | v1/users/requests | False | Fetch requests for a logged in user
GET | v1/users/requests/requestid | False | Fetch a request for a logged in user
PUT | v1/users/requests/requestid | False | Update a request for a logged in user

## Authors
[Bamuleseyo Gideon](https://github.com/lytes20)
