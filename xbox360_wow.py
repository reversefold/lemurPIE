
def do_action(keys):
    for down, key in keys:
        if down:
            keyboard.setKeyDown(key)
        else:
            keyboard.setKeyUp(key)

def action(keys):
    def action_closure():
        do_action(keys)
    return action_closure

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
        'a': [
            #button down
            action([ # list of keys
                [
                    True, # down? (False is up)
                    Key.D1 # actual key
                ],
            ]),
            #button up
            action([[False, Key.D1]])
        ],
        'b': [
            action([
                [True, Key.LeftShift],
                [True, Key.Grave],
                [False, Key.LeftShift],
            ]),
            action([
                [False, Key.Grave],
            ])
        ]
        #'x': Key.D2,
        #'y': Key.D3,
    }

class WoWController(object):
    def __init__(self):
        self.key_states = {}

    def tick(self):
        xbc = xbox360[0]
        for button, key in key_maps.iteritems():
            if getattr(xbc, button):
                #keyboard.setKeyDown(key)
                key[0]()
                self.key_states[button] = True
            elif self.key_states.get(button, False):
                #keyboard.setKeyUp(key)
                key[1]()
                self.key_states[button] = False
                """
                keyboard.setKeyDown(Key.LeftShift)
                keyboard.setKeyDown(key)
                keyboard.setKeyUp(key)
                keyboard.setKeyUp(Key.LeftShift)
                """
                
        for axis, keys in axis_maps.iteritems():
            axis_val = getattr(xbc, axis)
            key = None
            if axis_val < -AXIS_THRESHOLD:
                key = keys[0]
            elif axis_val > AXIS_THRESHOLD:
                key = keys[1]
            for ckey in keys:
                if ckey != key and self.key_states.get(ckey, False):
                    keyboard.setKeyUp(ckey)
                    self.key_states[ckey] = False
                    """
                    keyboard.setKeyDown(Key.LeftShift)
                    keyboard.setKeyDown(ckey)
                    keyboard.setKeyUp(ckey)
                    keyboard.setKeyUp(Key.LeftShift)
                    """
            if key is not None:
                keyboard.setKeyDown(key)
                self.key_states[key] = True

if starting:
    wow_controller = WoWController()
    
wow_controller.tick()
