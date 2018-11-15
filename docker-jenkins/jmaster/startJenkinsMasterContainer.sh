docker stop jenkins_master_DEV
docker rm jenkins_master_DEV

docker run -d -p 8080:8080 -p 50000:50000 -v $HOME/jenkins_home:/var/jenkins_home --name jenkins_master_DEV jenkins_master_image:v1.0.1
