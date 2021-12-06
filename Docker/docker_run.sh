#!/bin/bash

# Execute with sudo

s_DOCKER_IMAGE_NAME="sakib_mysql"

docker run -d -p 3306:3306 --name ${s_DOCKER_IMAGE_NAME} ${s_DOCKER_IMAGE_NAME}

echo "Showing running Instances"
docker ps
