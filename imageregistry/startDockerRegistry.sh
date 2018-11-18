echo "Starting docker registry on port 5100"
echo "Registry contents can be listed at http://localhost:5100/v2/_catalog"
echo "From containeers, this can be accessed as privaterepo"
docker run -d -p 5100:5000 --network parrot-net --restart=always --name privaterepo registry:2