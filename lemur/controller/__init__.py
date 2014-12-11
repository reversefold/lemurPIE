from lemur import Button


class Controller(object):
	def tick(self):
		for prop in self.__dict__.values():
			if isinstance(prop, Button):
				prop.tick()


class XBox360(Controller):
	def __init__(self, source):
		self.source = source
		self.start = Button(source, 'start')
		self.back = Button(source, 'back')
		self.a = Button(source, 'a')
		self.b = Button(source, 'b')
		self.x = Button(source, 'x')
		self.y = Button(source, 'y')
		self.leftShoulder = Button(source, 'leftShoulder')
		self.rightShoulder = Button(source, 'rightShoulder')
		self.leftThumb = Button(source, 'leftThumb')
		self.rightThumb = Button(source, 'rightThumb')
		# the d-pad acts like 4 buttons
		self.up = Button(source, 'up')
		self.down = Button(source, 'down')
		self.left = Button(source, 'left')
		self.right = Button(source, 'right')

		self.leftTrigger = None
		self.rightTrigger = None
		self.leftStick = None
		self.rightStick = None
