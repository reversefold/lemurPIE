if starting:
    import fplib
    fplib.keyboard = keyboard
    from fplib import *

#a, x, y, b
#1, 2, 3, 4
#5, 6, 7, 8
#9, 0, -, =
#Numpad 0, Numpad ., Sh-z, Sh-x

#b, Sh-`, Mouse 4, `
 
if starting:
    key_maps = {
        'a': Key.D1,
        'b': Key.D4,
        'x': Key.D2,
        'y': Key.D3,
    }
    axis_maps = {
        'leftStickY': [Key.S, Key.W],
        'leftStickX': [Key.A, Key.D],
    }
    AXIS_THRESHOLD = 0.3

    key_maps = {
        None: {
            'a': ButtonActions(
                KeyDown(Key.D1),
                KeyUp(Key.D1)
            ),
            'x': ButtonActions(Key.D2),
            'y': ButtonActions(Key.D3),
            'b': ButtonActions(Key.D4),
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
                self.current_map = key_map
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

if starting:
    wow_controller = WoWController(key_maps)
    
wow_controller.tick()
