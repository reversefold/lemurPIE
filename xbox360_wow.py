if starting:
    import math

    from lemur import *
    from lemur.action import *
    import lemur.action
    lemur.action.keyboard = keyboard
    lemur.action.mouse = mouse

#a, x, y, b
#1, 2, 3, 4
#5, 6, 7, 8
#9, 0, -, =
#Numpad 0, Numpad ., Sh-z, Sh-x

#b, Sh-`, Mouse 4, `

if starting:
    axis_maps = {
        'leftStickY': [Key.S, Key.W],
        'leftStickX': [Key.Q, Key.E],
    }
    AXIS_THRESHOLD = 0.4
    MOUSE_MULTIPLIER = 1.5

    key_maps = {
        None: {
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
            'up': ButtonActions(Key.NumberLock), #MouseButtonDown(3), MouseButtonUp(3)),
            'right': ButtonActions(Key.Grave),
            'back': ButtonActions(Key.M),
            'start': ButtonActions(Key.Tab),
        },
        'leftTrigger': {
            'a': ButtonActions(Key.D5),
            'x': ButtonActions(Key.D6),
            'y': ButtonActions(Key.D7),
            'b': ButtonActions(Key.D8),
        },
        'rightTrigger': {
            'a': ButtonActions(Key.D9),
            'x': ButtonActions(Key.D0),
            'y': ButtonActions(Key.Minus),
            'b': ButtonActions(Key.Equals),
        }
    }

class WoWController(object):
    def __init__(self, key_maps):
        self.key_maps = key_maps
        self.button_states = {}
        self.current_map = self.key_maps[None]

    def tick(self):
        xbc = xbox360[0]
        for button, key_map in self.key_maps.iteritems():
            if button is None:
                continue
            if getattr(xbc, button) > 0.25:
                self.current_map = dict(self.key_maps[None])
                self.current_map.update(key_map)
                self.button_states[button] = True
            elif self.button_states.get(button, False):
                self.current_map = self.key_maps[None]
                self.button_states[button] = False
        for button, key in self.current_map.iteritems():
            if getattr(xbc, button):
                #keyboard.setKeyDown(key)
                key.press()
                self.button_states[button] = True
            elif self.button_states.get(button, False):
                #keyboard.setKeyUp(key)
                key.release()
                self.button_states[button] = False

        for axis, keys in axis_maps.iteritems():
            axis_val = getattr(xbc, axis)
            key = None
            if axis_val < -AXIS_THRESHOLD:
                key = keys[0]
            elif axis_val > AXIS_THRESHOLD:
                key = keys[1]
            for ckey in keys:
                if ckey != key and self.button_states.get(ckey, False):
                    keyboard.setKeyUp(ckey)
                    self.button_states[ckey] = False
            if key is not None:
                keyboard.setKeyDown(key)
                self.button_states[key] = True

        if abs(xbc.rightStickX) > AXIS_THRESHOLD:
            mouse.deltaX = (abs(xbc.rightStickX) - AXIS_THRESHOLD) / (1.0 - AXIS_THRESHOLD) * MOUSE_MULTIPLIER * math.copysign(1, xbc.rightStickX) # * (0.5 if xbc.rightThumb else 1)
        if abs(xbc.rightStickY) > AXIS_THRESHOLD:
            mouse.deltaY = (abs(xbc.rightStickY) - AXIS_THRESHOLD) / (1.0 - AXIS_THRESHOLD) * MOUSE_MULTIPLIER * -math.copysign(1, xbc.rightStickY) # * (0.5 if xbc.rightThumb else 1)

if starting:
    wow_controller = WoWController(key_maps)

wow_controller.tick()
