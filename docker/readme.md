# docker on raspi

new sd card with new raspbian debian trixie. following is apparently giving a working docker cli

    noah@raspberrypi:~ $ history
        1  sudo apt-get update
        2  curl -sSL https://get.docker.com | sh
        3  sudo usermod -aG docker $USER
        4  docker

# utexas

prep the dsk folder in utexas/docker

    git clone https://gitlab.com/decwar/utexas.git
    cd utexas/docker
    unzip dsk-20251103.zip 
    mv dsk-20251103 dsk
    cd ..

docker build command

    sudo docker build -t utexas -f ./utexas.dockerfile .
    sudo docker run -d -p 2030:2030 --name utexas utexas

# merely-players

    sudo docker build -t merely-players -f ./merely-players.dockerfile .
    sudo docker run -d -p 2031:2031 --name merely-players merely-players

# galaxy

    sudo docker build -t galaxy -f ./galaxy.dockerfile .
    sudo docker run -d -p 2032:2032 --name galaxy galaxy
    sudo docker run -t -i -p 2032:2032 --name galaxy galaxy

# useful

    sudo docker images
    sudo docker ps
    sudo docker rm -f galaxy

noah@raspberrypi:~ $ sudo apt install telnet
noah@raspberrypi:~ $ telnet localhost 2030
