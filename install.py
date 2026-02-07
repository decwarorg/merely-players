"""
to install, create/copy and use install.py within the top-level folder where subfolders will be created

    python3 install.py [--latest for newest release]

to start the containers, use start.py in the merely-players subfolder

    cd merely-players
    python3 start.py [--latest for newest release]
"""
import os
import argparse

def main(args):
    if not os.path.exists('merely-players'): os.system('git clone https://github.com/decwarorg/merely-players.git')
    os.chdir('merely-players')
    if args.latest: os.system('python3 start.py --latest --norun')
    else: os.system('python3 start.py --norun')
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--latest", action="store_true")
    args = parser.parse_args()
    main(args)
    