class Error(Exception):
    pass


# sentinel for the State object
KEY = object()

class Button(object):
    """enum for the states in Button.state"""
    class State(object):
    	def __init__(self, lock, name):
    		if lock is not KEY:
    			raise Error("This object is not instantiatable")
    		self.name = name

    	def __str__(self):
    		return 'State(%s)' % (self.name,)

    	def __repr__(self):
    		return '%s.%s' % (self.name, super(Button.State, self).__repr__())

    def __init__(self, source_object, button_name):
        self.source_object = source_object
        self.button_name = button_name
        self._state = Button.State.UP

    @property
    def state(self):
       	return self._state

    def tick(self):
        val = getattr(self.source_object, self.button_name)
        if val:
            if self._state is Button.State.PRESSED or self._state is Button.State.DOWN:
                self._state = Button.State.DOWN
            else:
                self._state = Button.State.PRESSED
        elif self._state is Button.State.PRESSED or self._state is Button.State.DOWN:
            self._state = Button.State.RELEASED
        else:
            self._state = Button.State.UP

        return self.state

Button.State.UP = Button.State(KEY, 'UP')
Button.State.PRESSED = Button.State(KEY, 'PRESSED')
Button.State.DOWN = Button.State(KEY, 'DOWN')
Button.State.RELEASED = Button.State(KEY, 'RELEASED')

del KEY
