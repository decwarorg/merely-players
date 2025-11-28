"""
python3 build.py
  -n --nopull don't update utexas and galaxy repos using 'git reset --hard origin'
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
    os.chdir(pathroot() + '/..')
    if not os.path.exists('utexas'): os.system('git clone https://gitlab.com/decwar/utexas.git')
    os.chdir('utexas')
    if not args.nopull: pull()
    if not os.path.exists('docker/dsk'): os.system('unzip docker/dsk-20251103.zip && mv dsk-20251103 docker/dsk')
    os.chdir(pathroot() + '/..')
    if not os.path.exists('galaxy'): os.system('git clone https://gitlab.com/decwar/galaxy.git')
    os.chdir('galaxy')
    if not args.nopull: pull()
    os.system(f'docker compose  -f {pathroot()}/docker-compose.yaml up --build --force-recreate utexas cic galaxy')
    
def pull():
    os.system('git fetch')
    os.system('git reset --hard origin')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nopull", action="store_true")
    args = parser.parse_args()
    main(args)
