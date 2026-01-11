#!/bin/sh
echo '----------- myapp-Adaptor backend redeploy'
echo $USER
cd /home/$USER/DataScience/Django-Template-App/src
# git config credential.helper store
echo '----------- git pull'
sudo git reset --hard
sudo git pull

# cleanup docker
sudo docker stop myapp
sudo docker rm $(sudo docker container ls -aq --filter status=exited)
sudo docker image rm --force myapp-py:latest

# new image
echo '---------- creating new docker image'
sudo docker build -t myapp-py .
echo '--------- start docker image myapp-py container at port 8070'
sudo docker run -itd --name myapp -p 8070:8070 --restart=always myapp-py:latest

# test new container status
sleep 7
curl localhost:8070/myapp/test

echo '---------- push to gcr.io'
docker tag myapp-py gcr.io/conversational-ai-rnd/myapp-adaptor:v1
docker push gcr.io/conversational-ai-rnd/myapp-adaptor:v1

echo '---------- deploy to cloud run'
gcloud run deploy myapp-adaptor --image=gcr.io/conversational-ai-rnd/myapp-adaptor:v1 \
    --region=us-central1