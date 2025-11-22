"""
WARNING this can do git reset on current repo (merely-players). caution needed if you're coding there.
fix so docker doesn't need sudo https://docs.docker.com/engine/install/linux-postinstall/
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
docker compose exec cic sh
"""
import os
from cic.utils import pathroot

os.chdir(pathroot())
os.system('git fetch')
os.system('git reset --hard origin') # WARNING caution needed if you're coding
# os.system('docker rm -f cic') # probly best to manual, can slow things down a lot
os.system('docker build -t cic -f ./dockerfile-cic .')

os.chdir(pathroot() + '/..')
if not os.path.exists('galaxy'): os.system('git clone https://gitlab.com/decwar/galaxy.git')
os.chdir('galaxy')
os.system('git fetch')
os.system('git reset --hard origin')
os.system('docker build -t galaxy -f ./dockerfile-galaxy .')

os.chdir(pathroot() + '/..')
if not os.path.exists('utexas'): os.system('git clone https://gitlab.com/decwar/utexas.git')
os.chdir('utexas')
os.system('git fetch')
os.system('git reset --hard origin')
os.chdir('docker')
if not os.path.exists('dsk'):
    os.system('unzip dsk-20251103.zip') # this will eventually be unnecessary
    os.system('mv dsk-20251103 dsk')
os.chdir('..')
os.system('docker build -t utexas -f ./dockerfile-utexas .')
