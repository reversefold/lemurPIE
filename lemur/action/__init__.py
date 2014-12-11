from lemur import Error

class ActionError(Error):
    pass

class ActionNotExecutable(ActionError):
    pass

class InvalidAction(ActionError):
    pass


class Action(object):
    def __call__(self):
        pass


class SingleAction(Action):
    def __init__(self, action):
        if not callable(action):
            raise ActionNotExecutable()
        self.action = action

    def __call__(self):
        self.action()


class KeyDown(Action):
    def __init__(self, key):
        self.key = key

    def __call__(self):
        keyboard.setKeyDown(self.key)


class KeyUp(Action):
    def __init__(self, key):
        self.key = key

    def __call__(self):
        keyboard.setKeyUp(self.key)


class MouseButton(Action):
    def __init__(self, button, down):
        self.button = button
        self.down = down

    def __call__(self):
        mouse.setButton(self.button, self.down)


class MouseButtonDown(MouseButton):
    def __init__(self, button):
        super(MouseButtonDown, self).__init__(button, True)


class MouseButtonUp(MouseButton):
    def __init__(self, button):
        super(MouseButtonUp, self).__init__(button, False)


class Actions(Action):
    def __init__(self, *actions):
        if len(actions) == 1 and isinstance(actions[0], (list, tuple)):
            self.actions = list(actions[0])
        else:
            self.actions = list(actions)

    def __call__(self):
        for action in self.actions:
            action()


def make_action(action):
    if isinstance(action, Action):
        return action
    if isinstance(action, (list, tuple)):
        return Actions(*action)
    return SingleAction(action)


class ButtonActions(object):
    def __init__(self, press_action, release_action=None):
        if release_action is None:
            if isinstance(press_action, Action) or callable(press_action):
                raise InvalidAction("ButtonActions requires one key or two actions")
            release_action = KeyUp(press_action)
            press_action = KeyDown(press_action)

        if not isinstance(press_action, Action):
            press_action = make_action(press_action)
        if not isinstance(release_action, Action):
            release_action = make_action(release_action)

        self.press_action = press_action
        self.release_action = release_action

    def press(self):
        self.press_action()

    def release(self):
        self.release_action()
