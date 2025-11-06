import os
from merely_players.utils import pathroot

os.chdir(pathroot() + '/..')
# print(os.getcwd())
if not os.path.exists('galaxy'):
    os.system('git clone https://gitlab.com/decwar/galaxy.git')

os.chdir(pathroot() + '/../galaxy')
os.system('git fetch')
os.system('git reset --hard origin') # ensures we have current main branch
os.system('docker build -t galaxy -f ./galaxy.dockerfile .')

# for non docker compose
# os.system('docker rm -f galaxy')
# os.system('docker run -d -p 2032:2032 --name galaxy galaxy')

