from collections import OrderedDict
import math

from lemur import *
import lemur.action
from lemur.action import *
from lemur.trigger import TriggerThreshold

"""
a, x, y, b
1, 2, 3, 4
5, 6, 7, 8
9, 0, -, =
Numpad 0, Numpad ., Sh-z, Sh-x

b, Sh-`, Mouse 4, `
"""


def axis_maps(Key):
    return {
        'leftStickY': [Key.S, Key.W],
        'leftStickX': [Key.Q, Key.E],
    }

AXIS_THRESHOLD = 0.4
MOUSE_MULTIPLIER = 1.5
TRIGGER_THRESHOLD = 0.25


default_map_name = current_map_name = 'default'


class ChangeMap(SingleAction):
    def __init__(self, map_name):
        super(ChangeMap, self).__init__(self)
        self.map_name = map_name

    def __call__(self):
        global current_map_name
        current_map_name = self.map_name


def new_key_maps(Key):
    return OrderedDict([
        ('default', OrderedDict([
            ('a', ButtonActions(
                KeyDown(Key.D1),
                KeyUp(Key.D1)
            )),
            ('x', ButtonActions(Key.D2)),
            ('y', ButtonActions(Key.D3)),
            ('b', ButtonActions(Key.D4)),
            ('leftShoulder', ButtonActions(MouseButtonDown(0), MouseButtonUp(0))),
            ('rightShoulder', ButtonActions(MouseButtonDown(1), MouseButtonUp(1))),
            ('leftThumb', ButtonActions(Key.Space)),
            #('rightThumb', ButtonActions(MouseButtonDown(0), MouseButtonUp(0))),
            ('down', ButtonActions(Key.B)),
            ('left', ButtonActions(
                [
                    KeyDown(Key.LeftShift),
                    KeyDown(Key.Grave),
                    KeyUp(Key.LeftShift)
                ],
                KeyUp(Key.Grave)
            )),
            ('up', ButtonActions(Key.NumberLock)),  # MouseButtonDown(3), MouseButtonUp(3))),
            ('right', ButtonActions(Key.Grave)),
            ('back', ButtonActions(Key.M)),
            ('start', ButtonActions(Key.Tab)),
            (TriggerThreshold(controller.leftTrigger, TRIGGER_THRESHOLD),
                ButtonActions(ChangeMap('map2'), ChangeMap('default'))),
            (TriggerThreshold(controller.rightTrigger, TRIGGER_THRESHOLD),
                ButtonActions(ChangeMap('map3'), ChangeMap('default'))),
        ])),
        # left trigger held
        ('map2', OrderedDict([
            ('a', ButtonActions(Key.D5)),
            ('x', ButtonActions(Key.D6)),
            ('y', ButtonActions(Key.D7)),
            ('b', ButtonActions(Key.D8)),
            (TriggerThreshold(controller.rightTrigger, TRIGGER_THRESHOLD),
                ButtonActions(ChangeMap('map4'), ChangeMap('map2'))),
        ])),
        # right trigger held
        ('map3', OrderedDict([
            ('a', ButtonActions(Key.D9)),
            ('x', ButtonActions(Key.D0)),
            ('y', ButtonActions(Key.Minus)),
            ('b', ButtonActions(Key.Equals)),
            (TriggerThreshold(controller.leftTrigger, TRIGGER_THRESHOLD),
                ButtonActions(ChangeMap('map4'), ChangeMap('map3'))),
        ])),
        # both triggers held
        ('map4', OrderedDict([
            ('a', ButtonActions(Key.Apostrophe)),
            ('x', ButtonActions(Key.NumberPadPeriod)),
            ('y', ButtonActions(
                [KeyDown(Key.LeftShift), KeyDown(Key.Z), KeyUp(Key.LeftShift)],
                KeyUp(Key.Z)
            )),
            ('b', ButtonActions(
                [KeyDown(Key.LeftShift), KeyDown(Key.X), KeyUp(Key.LeftShift)],
                KeyUp(Key.X)
            )),
            # The Press actions here will never fire, these overrides are only here for the release actions
            (TriggerThreshold(controller.leftTrigger, TRIGGER_THRESHOLD),
                ButtonActions(ChangeMap('map2'), ChangeMap('map3'))),
            (TriggerThreshold(controller.rightTrigger, TRIGGER_THRESHOLD),
                ButtonActions(ChangeMap('map3'), ChangeMap('map2'))),
        ])),
    ])


def key_maps(Key):
    return OrderedDict([
        (None, {
            'a': ButtonActions(
                KeyDown(Key.D1),
                KeyUp(Key.D1)
            ),
            'x': ButtonActions(Key.D2),
            'y': ButtonActions(Key.D3),
            'b': ButtonActions(Key.D4),
            'leftShoulder': ButtonActions(MouseButtonDown(0), MouseButtonUp(0)),
            'rightShoulder': ButtonActions(MouseButtonDown(1), MouseButtonUp(1)),
            'leftThumb': ButtonActions(Key.Space),
            #'rightThumb': ButtonActions(MouseButtonDown(0), MouseButtonUp(0)),
            'down': ButtonActions(Key.B),
            'left': ButtonActions(
                [
                    KeyDown(Key.LeftShift),
                    KeyDown(Key.Grave),
                    KeyUp(Key.LeftShift)
                ],
                KeyUp(Key.Grave)
            ),
            'up': ButtonActions(
                [KeyDown(Key.LeftShift), KeyDown(Key.Backslash), KeyUp(Key.Backslash)],
                KeyUp(Key.Z)
            ),
            'right': ButtonActions(Key.Grave),
            'back': ButtonActions(Key.M),
            'start': ButtonActions(Key.Tab),
        }),
        ('leftTrigger', {
            'a': ButtonActions(Key.D5),
            'x': ButtonActions(Key.D6),
            'y': ButtonActions(Key.D7),
            'b': ButtonActions(Key.D8),
        }),
        ('rightTrigger', {
            'a': ButtonActions(Key.D9),
            'x': ButtonActions(Key.D0),
            'y': ButtonActions(Key.Minus),
            'b': ButtonActions(Key.Equals),
        }),
        ('leftTrigger,rightTrigger', {
            'a': ButtonActions(Key.Apostrophe),
            'x': ButtonActions(Key.NumberPadPeriod),
            'y': ButtonActions(
                [KeyDown(Key.LeftShift), KeyDown(Key.Z), KeyUp(Key.LeftShift)],
                KeyUp(Key.Z)
            ),
            'b': ButtonActions(
                [KeyDown(Key.LeftShift), KeyDown(Key.X), KeyUp(Key.LeftShift)],
                KeyUp(Key.X)
            ),
        }),
    ])


class WoWController(object):
    def __init__(self, controller, key_maps, axis_maps):
        self.key_maps = key_maps
        self.axis_maps = axis_maps
        self.controller = controller
        self.current_map = self.key_maps[None]
        self.button_states = {}

    def tick(self):
        self.controller.tick()

        for triggers, key_map in self.key_maps.iteritems():
            if triggers is None:
                continue
            triggersl = triggers.split(',')
            if all(getattr(self.controller, trigger).value > TRIGGER_THRESHOLD for trigger in triggersl):
                self.current_map = dict(self.key_maps[None])
                self.current_map.update(key_map)
                self.button_states[triggers] = True
            elif self.button_states.get(triggers, False):
                self.current_map = self.key_maps[None]
                self.button_states[triggers] = False

        for button_name, key in self.current_map.iteritems():
            button = getattr(self.controller, button_name)
            if button.state == Button.State.PRESSED:
                key.press()
            elif button.state == Button.State.RELEASED:
                key.release()

        for axis, keys in self.axis_maps.iteritems():
            axis_val = getattr(self.controller, axis)
            key = None
            if axis_val < -AXIS_THRESHOLD:
                key = keys[0]
            elif axis_val > AXIS_THRESHOLD:
                key = keys[1]
            for ckey in keys:
                if ckey != key and self.button_states.get(ckey, False):
                    KeyUp(ckey)()
                    self.button_states[ckey] = False
            if key is not None:
                KeyDown(key)()
                self.button_states[key] = True

        rsx = self.controller.rightStickX
        rsy = self.controller.rightStickY
        if abs(rsx) > AXIS_THRESHOLD:
            lemur.action.mouse.deltaX = (abs(rsx) - AXIS_THRESHOLD) / (1.0 - AXIS_THRESHOLD) * MOUSE_MULTIPLIER * math.copysign(1, rsx)  # * (0.5 if xbc.rightThumb else 1)
        if abs(rsy) > AXIS_THRESHOLD:
            lemur.action.mouse.deltaY = (abs(rsy) - AXIS_THRESHOLD) / (1.0 - AXIS_THRESHOLD) * MOUSE_MULTIPLIER * -math.copysign(1, rsy)  # * (0.5 if xbc.rightThumb else 1)

        if isinstance(lemur.action.mouse, Tickable):
            lemur.action.mouse.tick()
