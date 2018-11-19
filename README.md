# blueparrot
BlueParrot - A complete pipeline

# Create a network before deploying the containers

'''
createParrotNetwork.sh
'''

# Starting jenkins master using docker compose
This build and launches a jenins-master container.
'''
docker-compose -f docker-compose-tools.yml up -d
'''
Jenkins can be access as below
'''
http://localhost:8080
'''