# Call individual scripts to start the dockerised application
# This will not be required when using docker compose
./createParrotNetwork.sh
./ParrotApi/startParrotApi.sh
./ParrotDetailsApi/startParrotDetailsApi.sh
./BlueParrotWeb/startBlueParrotWeb.sh