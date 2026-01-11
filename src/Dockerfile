# pull images
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y
RUN apt-get clean

# change to home dir
ENV home_dir /home/ubuntu
WORKDIR ${home_dir}

# copy to current dir
COPY . .

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser ${home_dir}
USER appuser

# install requirements
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# migrate database
RUN python manage.py makemigrations\
    && python manage.py migrate \
    && python manage.py appinit

# entry point
EXPOSE 8070
CMD gunicorn --bind 0.0.0.0:8070  src.wsgi:application