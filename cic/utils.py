from pathlib import Path
import os
import subprocess

def pathroot():
    return str(Path(__file__).parent.parent)

def indocker():
    if os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False): return True
    return False

def latest_tag():
    os.system('git fetch --tags')
    latest = subprocess.getoutput("git describe --tags $(git rev-list --tags --max-count=1)")
    return latest
