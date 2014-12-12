class Error(Exception):
    pass


class Tickable(object):
	def tick(self):
		pass

# sentinel for the State object
KEY = object()

class Button(Tickable):
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


class Trigger(Tickable):
	def __init__(self, source_object, trigger_name):
		self.source_object = source_object
		self.trigger_name = trigger_name
		self._value = 0

	@property
	def value(self):
		return self._value

	def tick(self):
		self._value = getattr(self.source_object, self.trigger_name)
		return self._value


class Stick(Tickable):
	def __init__(self, source_object, x_axis_name, y_axis_name):
		self.source_object = source_object
		self.x_axis_name = x_axis_name
		self.y_axis_name = y_axis_name
		self._x = 0
		self._y = 0

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	def tick(self):
		self._x = getattr(self.source_object, self.x_axis_name)
		self._y = getattr(self.source_object, self.y_axis_name)
		return (self._x, self._y)
