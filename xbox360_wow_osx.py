import time

from lemur.osx import XBox360
from xbox360_wow import WowController

def main():
    controller = WowController(XBox360(0))
    while True:
        controller.tick()
        time.sleep(0.01)
