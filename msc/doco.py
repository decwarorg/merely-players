"""
WARNING about git reset on a repo. caution needed if you're coding in the repo.
cd into the merely-players folder
do the command 'python3 msc/doco.py' - this will prep docker compose
do the command 'docker compose up' - it will show console messages of the three containers starting
when the utexas container has reached 'GAM assigned' the dec10 is ready
open another terminal and connect to the cic container with 'docker compose exec cic sh'
in the cic container do 'python3 msc/robo.py' to start the robots
open another terminal and do 'telnet localhost 2030'
open a web browser to 'localhost:2031' for galaxy display
"""
import os
from cic.utils import pathroot

os.chdir(pathroot())
# os.system('git fetch')
# os.system('git reset --hard origin') # WARNING caution needed if you're coding in the repo
# os.system('docker rm -f cic') # for now, usually do manually
# os.system('docker image rm cic') # for now, usually do manually
os.system('docker build --check -t cic -f ./dockerfile-cic .') # --check is crucial right noe

os.chdir(pathroot() + '/..')
if not os.path.exists('galaxy'): os.system('git clone https://gitlab.com/decwar/galaxy.git')
os.chdir('galaxy')
os.system('git fetch')
os.system('git reset --hard origin') # WARNING caution needed if you're coding in the repo
# os.system('docker rm -f galaxy') # for now, usually do manually
os.system('docker build -t galaxy -f ./dockerfile-galaxy .')

os.chdir(pathroot() + '/..')
if not os.path.exists('utexas'): os.system('git clone https://gitlab.com/decwar/utexas.git')
os.chdir('utexas')
os.system('git fetch')
os.system('git reset --hard origin') # WARNING caution needed if you're coding in the repo
os.chdir('docker')
if not os.path.exists('dsk'):
    os.system('unzip dsk-20251103.zip') # this will eventually be unnecessary
    os.system('mv dsk-20251103 dsk')
os.chdir('..')
# os.system('docker rm -f utexas') # for now, usually do manually
os.system('docker build -t utexas -f ./dockerfile-utexas .')

"""
notes
fix so docker doesn't need sudo https://docs.docker.com/engine/install/linux-postinstall/
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
"""