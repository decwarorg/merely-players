"""
to install, run the install.py script in the folder where the decwar folders will live. to update with the latest code append '--update'
  python3 install.py
to run, run start.py within merely-players folder. to run with an update to the latest code append '--update'
  python3 start.py
"""
import os
import argparse

def main(args):
    if not os.path.exists('merely-players'): os.system('git clone https://gitlab.com/decwar/merely-players.git')
    os.chdir('merely-players')
    if args.update: os.system('python3 start.py --update --install')
    else: os.system('python3 start.py --install')
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--update", action="store_true")
    args = parser.parse_args()
    main(args)
    