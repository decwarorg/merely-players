"""
python3 build.py
  -p --pull updates utexas and galaxy repos using 'git reset --hard origin'
docker commands
  docker image rm cic utexas galaxy
  docker compose up
  docker compose exec cic /bin/bash
  docker compose down
within a cic container /bin/bash shell
  tail -f /data/log1
"""
import os
import argparse
from cic.utils import pathroot

def main(args):
    os.system('docker build -t cic -f ./dockerfile-cic .')
    
    os.chdir(pathroot() + '/..')
    if not os.path.exists('galaxy'): os.system('git clone https://gitlab.com/decwar/galaxy.git')
    os.chdir('galaxy')
    if args.pull: pull()
    os.system('docker build -t galaxy -f ./dockerfile-galaxy .')
    
    os.chdir(pathroot() + '/..')
    if not os.path.exists('utexas'): os.system('git clone https://gitlab.com/decwar/utexas.git')
    os.chdir('utexas')
    if args.pull: pull()
    if not os.path.exists('docker/dsk'): os.system('unzip docker/dsk-20251103.zip && mv dsk-20251103 docker/dsk')
    os.system('docker build -t utexas -f ./dockerfile-utexas .')
    
def pull():
    os.system('git fetch')
    os.system('git reset --hard origin')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pull", action="store_true")
    args = parser.parse_args()
    main(args)
    