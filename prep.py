import os
from cic.utils import pathroot

os.system('docker build -t cic -f ./dockerfile-cic .')

os.chdir(pathroot() + '/..')
if not os.path.exists('galaxy'): os.system('git clone https://gitlab.com/decwar/galaxy.git')
os.chdir('galaxy')
os.system('docker build -t galaxy -f ./dockerfile-galaxy .')

os.chdir(pathroot() + '/..')
if not os.path.exists('utexas'): os.system('git clone https://gitlab.com/decwar/utexas.git')
os.chdir('utexas')
if not os.path.exists('docker/dsk'): os.system('unzip docker/dsk-20251103.zip && mv dsk-20251103 docker/dsk')
os.system('docker build -t utexas -f ./dockerfile-utexas .')
