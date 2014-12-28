import keycode
import pygame
import Quartz

from lemur.controller import XBox360 as XBox360Base
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

class XBox360Source(Tickable):
    def __init__(self, idx=0):
        self.idx = idx
        pygame.init()
        self.joy = pygame.joystick.Joystick(idx)
        self.joy.init()

    def tick(self):
        pygame.event.pump()

    @property
    def up(self):
        return self.joy.get_button(0)

    @property
    def down(self):
        return self.joy.get_button(1)

    @property
    def left(self):
        return self.joy.get_button(2)

    @property
    def right(self):
        return self.joy.get_button(3)

    @property
    def start(self):
        return self.joy.get_button(4)

    @property
    def back(self):
        return self.joy.get_button(5)

    @property
    def leftThumb(self):
        return self.joy.get_button(6)

    @property
    def rightThumb(self):
        return self.joy.get_button(7)

    @property
    def leftShoulder(self):
        return self.joy.get_button(8)

    @property
    def rightShoulder(self):
        return self.joy.get_button(9)

    @property
    def xbox(self):
        return self.joy.get_button(10)

    @property
    def a(self):
        return self.joy.get_button(11)

    @property
    def b(self):
        return self.joy.get_button(12)

    @property
    def x(self):
        return self.joy.get_button(13)

    @property
    def y(self):
        return self.joy.get_button(14)

    @property
    def leftStickX(self):
        return self.joy.get_axis(0)

    @property
    def leftStickY(self):
        return -self.joy.get_axis(1)

    @property
    def rightStickX(self):
        return self.joy.get_axis(2)

    @property
    def rightStickY(self):
        return -self.joy.get_axis(3)

    @property
    def leftTrigger(self):
        return self.joy.get_axis(4)

    @property
    def rightTrigger(self):
        return self.joy.get_axis(5)


class XBox360(XBox360Base):
    def __init__(self, idx):
        super(XBox360, self).__init__(XBox360Source(idx))

    def tick(self):
        self.source.tick()
        super(XBox360, self).tick()


class Keyboard(object):
    def keyboard_event(self, keycode, down):
        # TODO: do we need to generate this every time?
        source = Quartz.CGEventSourceCreate(Quartz.kCGEventSourceStateCombinedSessionState)
        Quartz.CGEventPost(Quartz.kCGAnnotatedSessionEventTap,
            Quartz.CGEventCreateKeyboardEvent(source, keycode, down))

    def setKeyDown(self, key):
        self.keyboard_event(key, True)

    def setKeyUp(self, key):
        self.keyboard_event(key, False)


class Mouse(object):
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.leftDown = False
        self.rightDown = False

    def mouse_event(self, type, button):
        Quartz.CGEventPost(
            Quartz.kCGHIDEventTap,
            Quartz.CGEventCreateMouseEvent(
                    None,
                    type,
                    (self.posx, self.posy),
                    button))

    def setButton(self, idx, down):
        if idx == 0:
            self.leftDown = down
        elif idx == 1:
            self.rightDown = down
        self.mouse_event(
            (Quartz.kCGEventLeftMouseDown if down else Quartz.kCGEventLeftMouseUp) if idx == 0
                else (Quartz.kCGEventRightMouseDown if down else Quartz.kCGEventRightMouseUp),
            Quartz.kCGMouseButtonLeft if idx == 0 else Quartz.kCGMouseButtonRight
        )

    def mouse_moved(self):
        self.mouse_event(Quartz.kCGEventLeftMouseDragged if self.leftDown else (Quartz.kCGEventRightMouseDragged if self.rightDown else Quartz.kCGEventMouseMoved),
            Quartz.kCGMouseButtonRight if self.rightDown else Quartz.kCGMouseButtonLeft)

    @property
    def deltaX(self):
        return 0

    @deltaX.setter
    def deltaX(self, value):
        self.posx += value * 3
        self.posx = max(0, self.posx)
        self.mouse_moved()

    @property
    def deltaY(self):
        return 0

    @deltaY.setter
    def deltaY(self, value):
        self.posy += value  * 3
        self.posy = max(0, self.posy)
        self.mouse_moved()


class Key(object):
    A = keycode.tokeycode('a')
    B = keycode.tokeycode('b')
    C = keycode.tokeycode('c')
    D = keycode.tokeycode('d')
    E = keycode.tokeycode('e')
    F = keycode.tokeycode('f')
    G = keycode.tokeycode('g')
    H = keycode.tokeycode('h')
    I = keycode.tokeycode('i')
    J = keycode.tokeycode('j')
    K = keycode.tokeycode('k')
    L = keycode.tokeycode('l')
    M = keycode.tokeycode('m')
    N = keycode.tokeycode('n')
    O = keycode.tokeycode('o')
    P = keycode.tokeycode('p')
    Q = keycode.tokeycode('q')
    R = keycode.tokeycode('r')
    S = keycode.tokeycode('s')
    T = keycode.tokeycode('t')
    U = keycode.tokeycode('u')
    V = keycode.tokeycode('v')
    W = keycode.tokeycode('w')
    X = keycode.tokeycode('x')
    Y = keycode.tokeycode('y')
    Z = keycode.tokeycode('z')
    D1 = keycode.tokeycode('1')
    D2 = keycode.tokeycode('2')
    D3 = keycode.tokeycode('3')
    D4 = keycode.tokeycode('4')
    D5 = keycode.tokeycode('5')
    D6 = keycode.tokeycode('6')
    D7 = keycode.tokeycode('7')
    D8 = keycode.tokeycode('8')
    D9 = keycode.tokeycode('9')
    D0 = keycode.tokeycode('0')
    Space = keycode.tokeycode(' ')
    Grave = keycode.tokeycode('`')
    Minus = keycode.tokeycode('-')
    Equals = keycode.tokeycode('=')
    Apostrophe = keycode.tokeycode("'")
    Tab = keycode.tokeycode("\t")  # 0x30
    CapsLock = 0x39
    #NumberLock
    NumberPadPeriod = 0x41
    LeftShift = 0x38
