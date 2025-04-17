# command to copy all the libraries of an application
pip freeze >> requirements.txt
# command to build docker images
docker build -t testimage .
# command to list out local images on your machine
docker images
# command to delete image
docker rmi image testimage
# command to create a container
docker run -d -p 5009:5009 diamondimage1:latest
# command to bring up the running containers
docker ps
# command to show all the running and stopped container
docker ps
# command to stop a container from running
docker stop
# command to create a new container
docker run --name champion -dp 5008:5008 seunimage:latest
# command to exec into a container
docker exec -it container-name sh
# command to exit the container
exit