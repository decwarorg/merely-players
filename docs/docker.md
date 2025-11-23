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

# notes

reattaching i get :
Connected to the KL-10 simulator TTY device, line 0
and things sem SLLLLOW
like the time command takes a couple minutes ot display
Noah — 08:19
maybe i'm misunderstanding - you're seeing a difference between connections? 🤔 
strange - have not seen that - and usually have ten python robots playing - has always seemed fine when i jump in 🤔
guess can say - in those youtube 'bad vids' have made, you can see me playing, and that's what looks/feels normal for me - have not seen any major issues - hmmm, there are occasional oddities but can even remember those from back in the day - it was never smooth as modern systems 
Noah — 08:33
have not seen any kind of 'overall slowness'
am in game with ten robots and two ships of my own right now - all seems normal
Noah — 08:41
hmmm, weird thought - maybe it's because of the ten robots that have not seen anything unusual? they're driving the action in some sense, for sure - maybe they play some kind of role am not even aware of 🤔 

hmmm, nother thought - what could be somehow 'special' so that have not seen anything odd here on mac or raspi 
possibility - have never tried for 'uptime' of the dec10
have pretty much always been fresh starting dec10 to start a game
these days, to have a game, pretty much always do 'docker compose up' - 
or the equivalent in the docker gui - hitting the start button there
maybe if the dec10 has been 'up' - it's gathering uptime - it gets into a weird state?
haven't seen it myself but can speculate 🙂
with docker just shut it down any time - start it up anytime - all super easy and light weight  - it's a dedicated single shot single game type deal, not an 'uptime' deal - 'disposable dec10' 

