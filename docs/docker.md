# docker on raspi

new sd card with new raspbian debian trixie. following is giving a working docker cli

    sudo apt-get update
    curl -sSL https://get.docker.com | sh
    sudo usermod -aG docker $USER

also note for raspi

    noah@raspberrypi:~ $ sudo apt install telnet
    noah@raspberrypi:~ $ telnet localhost 2030

# for docker get rid of sudo

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

    docker images
    docker ps
    docker rm -f galaxy
    docker rm -f galaxy
    docker run -d -p 2032:2032 --name galaxy galaxy
