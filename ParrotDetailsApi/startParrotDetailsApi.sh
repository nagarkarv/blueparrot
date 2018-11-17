docker stop parrot_details_api_dev
docker rm parrot_details_api_dev

docker run -d -p5001:5001 --name parrot_details_api_dev parrot_details_api:v1.0.0
