# Django Template Application
![django](document/image/python-django.png)

## Application Feature.
1. Django REST API
2. JWT Token autherization
3. Docker file
4. Deployment shell script
5. Serving static file by enabling debug mode
6. Allow cross origin header
7. write logs to console, file.
8. Django model, serializer

# Application Setup Intructions
1. Creating a repository from a template
2. Environment file
3. Configuration file
4. Authorization
5. Management command
6. Docker Container
7. Clone Repository
8. Usefull commands


## 1. Creating a repository from a template
* On GitHub.com, navigate to the main page of the repository.
* Above the file list, click Use this template.
* Use the Owner drop-down menu, and select the account you want to own the repository.
* Type a name for your repository, and an optional description.

Please flow below link to 
[Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)


## 2. Environment file
The environment file will be stored in config folder. It will be ignored while committing to GitHub, for security reasons. We can ignore any file by mentioning those file names in `.gitignore` file.

### content in environ.json
```python
{
    "SECRET_KEY":"xxxx",
    "DEBUG":"1",
    "ALLOWED_HOSTS":"*,0.0.0.0,127.0.0.1,localhost",
    "username":"xxxx",
    "password":"xxx",
    "email":"xxx@atos.net"
}
```
## 3. Configuration file
In configuration file we will mention different configuration for application. It could be different external API URL, parameters, headers. 
### content in config.json
```python
{
   "integration_api":{
        "baseUrl":"https://api.com",
        "message_api":{
            "method":"GET",
            "api":"{baseUrl}/messages/{messageId}",
            "headers":{
                "Authorization": "{token_type} {access_token}"
            }
        },
        "auth_api":{
            "method":"POST",
            "api":"{baseUrl}/2.0/token",
            "headers":{
                "Content-Type":"application/json"
            },
            "data":{
                "client_id":"xxxx",
                "client_secret":"xxxxx"
            }
        }
   }
}
```

## 4. Authorization
To create new super user for application, we need to use uuid library to generate new unique username and password. Alternatively, we can create simple username and password, but it would be good practice to use uuid library. So, it will be safe and secure.

1. create username and password using `uuid` library
2. copy username and password to `environ.json` file
3. run ` python manage.py appinit`, we have management command in application. It will automatically create new super user.

### Create new super user
```python
import uuid
username = str(uuid.uuid4())[0:18]
password = str(uuid.uuid4())
print("\nusername: {username} \npassword: {password}")
```

## 5. Management command
We written management command to create new super user. It is we help when we want to create fresh docker container. We can also add new function base on our requirements. It will run only once while we create docker container. 

* run ` python manage.py appinit`
* py file path `src\myapp\management\commands\appinit.py`


## 6. Docker Container
The `Dockerfile` is used create new container. First we need to change port number in the file, if mulitple containers in Virtual machine. If want to change python version, that also can be change in that file. There are few shell scripts in scripts folder. If want to host application in VM use `project_redeploy.sh` file and in GCP cloud run use `project_gcp.sh`. We can also rename those file to our project name.

Once required changes are made, make git commit.

* create docker file by running `sh project_redeploy.sh` 
* file path `src\scripts\project_redeploy.sh`

## 7. Clone Repository
Create in one folder in home directory as `DataScience`. /home/$USER/DataScience. clone the project repositry inside DataScience folder. 

## 8. Usefull commands
```shell
# Create new folder
mkdir DataScience

# navigate to new folder
cd DataScience

# clone repositroy 
git clone https://github.gsissc.myatos.net/IN-BLR-AIAP/NEW-PROJECT

# create new file copy content using vim editior
vi environ.json
touch environ.json

# remove file
rm -rf environ.json

# create file shortcut in linux
ln -n  DataScience/NEW-PROJECT/src/scripts/project_gcp.sh

# deploy to GCP cloud run
sh project_gcp.sh

# redeploy/deploy in Virtual Machine
sh project_redeploy.sh
```

# Reference
* [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
* [Django 3.2.10](https://docs.djangoproject.com/en/3.2/)
* [Django-rest-framework](https://www.django-rest-framework.org/)
* [Docker](https://docs.docker.com/)
* [JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* [Conda Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [Custom management commands](https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/)