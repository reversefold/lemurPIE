import pygame
import Quartz

from lemur import Tickable

"""
Buttons:
0  up
1  down
2  left
3  right
4  start
5  back
6  leftStick
7  rightStick
8  leftBumper
9  rightBumper
10 xbox
11 a
12 b
13 x
14 y

Axes:
0 leftStickX   -1 (left) 1 (right)
1 leftStickY   -1 (up) 1 (down)
2 rightStickX  -1 (left) 1 (right)
3 rightStickY  -1 (up) 1 (down)
4 leftTrigger  1 (pressed) -1 (released)
5 rightTrigger 1 (pressed) -1 (released)
"""

class XBox360(Tickable):
    def __init__(self, idx=0):
        self.idx = idx
        pygame.init()
        self.joy = pygame.joystick.Joystick(idx)
        self.joy.init()

    def tick(self):
        pygame.event.pump()

    @property
    def up(self):
        return joy.get_button(0)

    @property
    def down(self):
        return joy.get_button(1)

    @property
    def left(self):
        return joy.get_button(2)

    @property
    def right(self):
        return joy.get_button(3)

    @property
    def start(self):
        return joy.get_button(4)

    @property
    def back(self):
        return joy.get_button(5)

    @property
    def leftStick(self):
        return joy.get_button(6)

    @property
    def rightStick(self):
        return joy.get_button(7)

    @property
    def leftBumper(self):
        return joy.get_button(8)

    @property
    def rightBumper(self):
        return joy.get_button(9)

    @property
    def xbox(self):
        return joy.get_button(10)

    @property
    def a(self):
        return joy.get_button(11)

    @property
    def b(self):
        return joy.get_button(12)

    @property
    def x(self):
        return joy.get_button(13)

    @property
    def y(self):
        return joy.get_button(14)

    @property
    def leftStickX(self):
        return joy.get_axis(0)

    @property
    def leftStickY(self):
        return joy.get_axis(0)

    @property
    def rightStickX(self):
        return joy.get_axis(0)

    @property
    def rightStickY(self):
        return joy.get_axis(0)

    @property
    def leftTrigger(self):
        return joy.get_axis(0)

    @property
    def rightTrigger(self):
        return joy.get_axis(0)

xbox360 = [XBox360()]
