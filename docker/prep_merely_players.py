import os
from merely_players.utils import pathroot

# usually we're already inside merely players and are manually controlling git
# os.chdir(pathroot() + '/..')
# # print(os.getcwd())
# if not os.path.exists('merely-players'):
#     os.system('git clone https://gitlab.com/decwar/merely-players.git')
# os.chdir(pathroot())
# os.system('git fetch')
# os.system('git reset --hard origin') # ensures we have current main branch

os.system('docker build -t merely-players -f ./merely-players.dockerfile .')

# for non docker compose
# os.system('docker rm -f merely-players')
# os.system('docker run -d -p 2031:2031--name merely-players merely-players')

