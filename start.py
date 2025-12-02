"""
to start the containers, use start.py in the merely-players subfolder

    cd merely-players
    python3 start.py [--latest for newest release]
"""
import os
import argparse
from cic.utils import pathroot, latest_tag

def main(args):
    
    os.chdir(pathroot())
    if args.reset: reset(args)

    os.chdir(pathroot() + '/..')
    if not os.path.exists('utexas'): os.system('git clone https://gitlab.com/decwar/utexas.git')
    os.chdir('utexas')
    if args.reset: reset(args)
    if not os.path.exists('docker/dsk'): os.system('unzip docker/dsk-20251103.zip && mv dsk-20251103 docker/dsk')

    os.chdir(pathroot() + '/..')
    if not os.path.exists('galaxy'): os.system('git clone https://gitlab.com/decwar/galaxy.git')
    os.chdir('galaxy')
    if args.reset: reset(args)

    os.chdir(pathroot())
    if not args.norun: os.system(f'docker compose up --build --force-recreate utexas cic galaxy')
    
def reset(args):
    os.system('git fetch')
    os.system('git reset --hard origin')  # warning this overwrites local changes
    if args.latest: os.system(f'git checkout {latest_tag()}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--latest", action="store_true")
    parser.add_argument("--reset", action="store_true")
    parser.add_argument("--norun", action="store_true")
    args = parser.parse_args()
    if args.latest: args.reset = True
    main(args)
