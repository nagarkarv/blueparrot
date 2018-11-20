# Blueparrot
BlueParrot - A complete dockerised pipeline which includes an integration of various tool. There are no static configurations except for what has been provided in the docker compose files. For simplicity this has been tested on a single host.

- Jenkins Master
- On Demand Jenkins Linux Slave
- Jenkins Plugins management
- Pipeline as Code
- Dockerised Python API and Web App
- Docker Compose to manage containers
- Docker repository
- Prometheus (Container monitoring)

# Steps
# Create a network before deploying the containers
All containers attach to a custom network 'parrot-net'
```
createParrotNetwork.sh
```
# Spin up containers for supporting Toolset (using docker compose)
Note: Each project has a set of .bat files which can be used if you want to try them without using docker compose

```
docker-compose -f docker-compose-tools.yml up -d
```

This builds and launches the following tools within its own containers

- Jenkins Master
```
http://localhost:8080)
```
- Docker private registry
- Prometheus 

```
docker-compose -f docker-compose-app.yml up -d
```
