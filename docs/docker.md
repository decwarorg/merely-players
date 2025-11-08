# docker on raspi

new sd card with new raspbian debian trixie. following is giving a working docker cli

    sudo apt-get update
    curl -sSL https://get.docker.com | sh
    sudo usermod -aG docker $USER

# useful

    docker images
    docker ps
    docker rm -f galaxy

noah@raspberrypi:~ $ sudo apt install telnet
noah@raspberrypi:~ $ telnet localhost 2030
