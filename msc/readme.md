
# get rid of sudo

https://docs.docker.com/engine/install/linux-postinstall/

    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
    docker run hello-world

# useful docker compose

    docker compose down
    docker compose pull
    docker compose up

# useful non docker compose

    docker rm -f galaxy
    docker run -d -p 2032:2032 --name galaxy galaxy
