"""
WARNING this can do git reset on current repo (merely-players). caution needed if you're coding there.
fix so docker doesn't need sudo https://docs.docker.com/engine/install/linux-postinstall/
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
"""
import os
from cic.utils import pathroot

os.chdir(pathroot())
os.system('git fetch')
os.system('git reset --hard origin') # WARNING caution needed if you're coding
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
os.system('docker build -t utexas -f ./dockerfile-utexas .')
