"""
to run, run start.py within merely-players folder. to run with an update to the latest code append '--update'
  python3 start.py
"""
import os
import argparse
from cic.utils import pathroot

def main(args):
    # prep merely-players folder
    os.chdir(pathroot())
    if args.update: update()
    # prep utexas folder
    os.chdir(pathroot() + '/..')
    if not os.path.exists('utexas'): os.system('git clone https://gitlab.com/decwar/utexas.git')
    os.chdir('utexas')
    if args.update: update()
    if not os.path.exists('docker/dsk'): os.system('unzip docker/dsk-20251103.zip && mv dsk-20251103 docker/dsk')
    # prep galaxy folder
    os.chdir(pathroot() + '/..')
    if not os.path.exists('galaxy'): os.system('git clone https://gitlab.com/decwar/galaxy.git')
    os.chdir('galaxy')
    if args.update: update()
    # docker compose up for the complete system
    os.chdir(pathroot())
    if not args.install: os.system(f'docker compose up --build --force-recreate utexas cic galaxy')
    
def update():
    os.system('git fetch')
    os.system('git reset --hard origin') # warning this overwrites local changes

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--install", action="store_true")
    args = parser.parse_args()
    main(args)
