from lemur import Button, Tickable, Trigger, Stick


class Controller(Tickable):
	def tick(self):
		for prop in self.__dict__.values():
			if isinstance(prop, Tickable):
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

		self.leftTrigger = Trigger(source, 'leftTrigger')
		self.rightTrigger = Trigger(source, 'rightTrigger')
		self.leftStick = Stick(source, 'leftStickX', 'leftStickY')
		self.rightStick = Stick(source, 'rightStickX', 'rightStickY')

	@property
	def leftStickX(self):
		return self.leftStick.x

	@property
	def leftStickY(self):
		return self.leftStick.y

	@property
	def rightStickX(self):
		return self.rightStick.x

	@property
	def rightStickY(self):
		return self.rightStick.y
