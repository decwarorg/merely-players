from pathlib import Path
import os

def pathroot():
    return str(Path(__file__).parent.parent)

def indocker():
    if os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False): return True
    return False
