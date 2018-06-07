## Important terms
* image: asset
* container: an instance of running image with configured resources and other properties
* service: Services are really just “containers in production.” A service only runs one image, but it codifies the way that image runs—what ports it should use, how many replicas of the container should run so the service has the capacity it needs, and so on
* swarm: a dockerized cluster
* swarm-manager: the only machine in a swarm that can execute your commands, or authorize other machines to join the swarm as workers
* stack: a group of interrelated services that share dependencies, and can be orchestrated and scaled together.

## Various files:
* Dockerfile.yml: defines an image
* docker-compose.yml: defines a service (essentially how should the image be run - read service above)
* requirements.txt: list of modules to be installed

## Naming at multiple levels
* image has a name
* container (i.e. an instance of an image) can be given a name
* service: name given in docker_compose file (is appended with the stack name as set when deploying and the instance number)
* stack can be given a name while deploying (which names all underlying services with stackName_<serviceName>)

### Commands to start the swarm and deploy services

```
# Build image
docker build -t friendlyhello .

# tag image to push to image hub
docker tag friendlyhello smahajan12/friendlyhello:0.1

# push the image to docker hub
docker push smahajan12/friendlyhello:0.1

# start the swarm
docker swarm init

# deploy the services with stack name 
docker stack deploy -c docker-compose.yml <stackname>

# list all the services
docker service ls

# shutdown the services
docker stack rm <stackname>

# close the swarm
docker swarm leave --force
```
