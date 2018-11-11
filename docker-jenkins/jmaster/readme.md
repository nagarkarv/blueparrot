
# Docker Jenkins Master
- Create a Volume for jenkins home
-- mdir $HOME/jenkins_home
-- chown 1000 $HOME/jenkins_home

- Start the container using the start.sh script
- Use the groovy script to generate a list of plugins from an existing jenkins instance and then manage configuration as code

# Enable remote api for docker 
For me worked on Ubuntu 18.04.1 LTS and Docker 18.06.0-ce create /etc/systemd/system/docker.service.d/remote-api.conf with following content:

[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2376 -H unix:///var/run/docker.sock

then run sudo systemctl daemon-reload and sudo systemctl restart docker See result calling:

curl http://localhost:2376/info

Ref: https://stackoverflow.com/questions/42987692/docker-enable-remote-http-api-with-systemd-and-daemon-json

Test connection from docker plugin returns - Version = 18.06.1-ce, API Version = 1.38