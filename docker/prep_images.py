# docker compose
# docker compose down
# docker compose pull
# docker compose up
import os
from cic.utils import pathroot

os.chdir(pathroot())
os.system('git fetch')
os.system('git reset --hard origin')
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

# for non docker compose
# os.system('docker rm -f galaxy')
# os.system('docker run -d -p 2032:2032 --name galaxy galaxy')

