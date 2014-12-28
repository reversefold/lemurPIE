import time

import lemur.action
from lemur.osx import XBox360, Keyboard, Mouse, Key
from lemur.xbox360_wow import key_maps, axis_maps, WoWController

# TODO: If the controller disconnects, we lose the input


def main():
    lemur.action.keyboard = Keyboard()
    lemur.action.mouse = Mouse()

    controller = WoWController(XBox360(0), key_maps(Key), axis_maps(Key))
    while True:
        controller.tick()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
