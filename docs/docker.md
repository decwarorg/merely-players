# docker on raspi

new sd card with new raspbian debian trixie. following is giving a working docker cli

    sudo apt-get update
    curl -sSL https://get.docker.com | sh
    sudo usermod -aG docker $USER

# utexas

prep the dsk folder in utexas/docker

    git clone https://gitlab.com/decwar/utexas.git
    cd utexas/docker
    unzip dsk-20251103.zip 
    mv dsk-20251103 dsk
    cd ..
    docker build -t utexas -f ./utexas.dockerfile .
    docker run -d -p 2030:2030 --name utexas utexas

# merely-players

    docker build -t merely-players -f ./merely-players.dockerfile .
    docker run -d -p 2031:2031 --name merely-players merely-players

# galaxy

    docker build -t galaxy -f ./galaxy.dockerfile .
    docker run -d -p 2032:2032 --name galaxy galaxy
    docker run -t -i -p 2032:2032 --name galaxy galaxy

# useful

    docker images
    docker ps
    docker rm -f galaxy

noah@raspberrypi:~ $ sudo apt install telnet
noah@raspberrypi:~ $ telnet localhost 2030
