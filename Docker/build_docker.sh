#!/bin/bash

# Execute with sudo

s_DOCKER_IMAGE_NAME="sakib_mysql"

printf "Stopping old image %s\n" "${s_DOCKER_IMAGE_NAME}"
sudo docker stop sakib_mysql

printf "Removing old image %s\n" "${s_DOCKER_IMAGE_NAME}"
sudo docker rm "${s_DOCKER_IMAGE_NAME}"

printf "Creating Docker Image %s\n" "${s_DOCKER_IMAGE_NAME}"
sudo docker build -t sakib_mysql . --no-cache

i_EXIT_CODE=$?
if [ $i_EXIT_CODE -ne 0 ]; then
    printf "Error. Exit code %s\n" ${i_EXIT_CODE}
    exit
fi

echo "Ready to run ${s_DOCKER_IMAGE_NAME} Docker Container"
echo "To run type: sudo docker run -d -p 3306:3306 --name ${s_DOCKER_IMAGE_NAME} ${s_DOCKER_IMAGE_NAME}"
echo "or just use run_in_docker.sh"
echo
echo "Debug running Docker:"
echo "docker exec -it ${s_DOCKER_IMAGE_NAME} /bin/bash"
echo
