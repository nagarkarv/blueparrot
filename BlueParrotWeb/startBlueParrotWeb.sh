docker stop blueparrot_web_dev
docker rm blueparrot_web_dev

docker run -d -p5002:5002 --link parrot_details_api_dev:parrot_details_api_dev --link parrot_api_dev:parrot_api_dev --name blueparrot_web_dev blueparrot_web:v1.0.0
