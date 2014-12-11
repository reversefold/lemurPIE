from lemur import Error

class TriggerError(Error):
	pass


class Trigger(object):
    def __call__(self):
        return False
