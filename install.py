"""
put/create this install.py script file in a folder where you want the decwar repos to live
cd into that folder and use python to run this script, command is 'python3 install.py' on my mac
docker compose will bring up the containers and do a fresh build of utexas decwar
when it reaches 'utexas-1  | GAM assigned' it's finished and ready
open a terminal and do 'telnet localhost 2030' (may need to 'brew install telnet' on some macs)
"""
import os
import argparse

def main(args):
    if not os.path.exists('merely-players'): os.system('git clone https://gitlab.com/decwar/merely-players.git')
    os.chdir('merely-players')
    os.system('git fetch')
    os.system('git reset --hard origin')
    os.system('python3 start.py')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
    