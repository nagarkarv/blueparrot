# legacy way to connect using --link
#docker run -d -p5002:5002 --link parrot_details_api_dev:parrot_details_api_dev --link parrot_api_dev:parrot_api_dev --name blueparrot_web_dev blueparrot_web:v1.0.0

# rather connect using user defined networks
docker run -d -p5002:5002 --network parrot-net --name blueparrot_web_dev blueparrot_web:v1.0.0
