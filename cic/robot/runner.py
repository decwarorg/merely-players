"""
docker compose exec cic sh
useful commands when robots are running
tail -f log1
pkill -[signal # or name] -f python
2  SIGINT  ctrlc   
20 SIGTSTP ctrlz
"""
import os
import glob
import time
from cic.utils import pathroot


def start():
    os.chdir(pathroot())
    files = glob.glob('data/log*')
    for file in files: os.remove(file)
    
    os.system('python3 -u cic/robot/robot.py > data/log1 &')
    time.sleep(2)
    os.system('python3 -u cic/robot/robot.py -n robot2 > data/log2 &')
    time.sleep(5)
    os.system('python3 -u cic/robot/robot.py -n robot3 > data/log3 &')
    time.sleep(5)
    os.system('python3 -u cic/robot/robot.py -n robot4 > data/log4 &')
    time.sleep(5)
    os.system('python3 -u cic/robot/robot.py -n robot5 > data/log5 &')
    time.sleep(5)
    os.system('python3 -u cic/robot/robot.py -n robot6 > data/log6 &')
    time.sleep(5)
    os.system('python3 -u cic/robot/robot.py -n robot7 > data/log7 &')
    time.sleep(5)
    os.system('python3 -u cic/robot/robot.py -n robot8 > data/log8 &')
    time.sleep(5)
    os.system('python3 -u cic/robot/robot.py -n robot9 > data/log9 &')
    time.sleep(5)
    os.system('python3 -u cic/robot/robot.py -n robot10 > data/log10 &')
    time.sleep(5)
    
def stop():
    os.system('pkill -2 -f python')

if __name__ == "__main__":
    start()
    