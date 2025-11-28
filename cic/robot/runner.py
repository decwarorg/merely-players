import os
import glob
import time
from cic.utils import pathroot

def start(pop=10):
    os.chdir(pathroot())
    files = glob.glob('data/log*')
    for file in files: os.remove(file)
    for id in range(1, pop+1):
        name = f'robot{id}' if id > 2 else 'nomad'
        os.system(f'python3 -u cic/robot/robot.py -n {name} > data/log{id} &')
        time.sleep(5)
    
def stop():
    os.system("pkill -2 -f 'robot/robot.py'")
    time.sleep(5)

if __name__ == "__main__":
    start()
    