docker stop parrot_api_dev
docker rm parrot_api_dev

docker run -d -p5000:5000 --name parrot_api_dev parrot_api:v1.0.0
