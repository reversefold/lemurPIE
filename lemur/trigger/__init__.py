from lemur import Error


class TriggerError(Error):
	pass


class Trigger(object):
    def __call__(self):
        return False


class TriggerThreshold(Trigger):
	def __init__(self, trigger, threshold):
		self.trigger = trigger
		self.threshold = threshold

	def __call__(self):
		return self.trigger.value > threshold
