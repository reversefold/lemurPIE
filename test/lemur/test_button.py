import mox
import unittest

from lemur import Button


class TestButton(mox.MoxTestBase):
	def setUp(self):
		super(TestButton, self).setUp()
		self.controller = self.mox.CreateMockAnything()
		self.controller.a = False
		self.button = Button(self.controller, 'a')

	def test_initial_state(self):
		self.assertEquals(self.button(), Button.State.UP)

	def test_state_unchanged(self):
		self.assertEquals(self.button(), Button.State.UP)
		self.assertEquals(self.button(), Button.State.UP)

	def test_transition_up_to_pressed(self):
		self.assertEquals(self.button(), Button.State.UP)
		self.controller.a = True
		self.assertEquals(self.button(), Button.State.PRESSED)

	def test_transition_pressed_to_down(self):
		self.test_transition_up_to_pressed()
		self.assertEquals(self.button(), Button.State.DOWN)

	def tets_down_unchanged(self):
		self.test_transition_pressed_to_down()
		self.assertEquals(self.button(), Button.State.DOWN)

	def test_transition_down_to_released(self):
		self.test_transition_pressed_to_down()
		self.controller.a = False
		self.assertEquals(self.button(), Button.State.RELEASED)

	def test_transition_released_to_up(self):
		self.test_transition_down_to_released()
		self.assertEquals(self.button(), Button.State.UP)

	def test_transition_up_unchanged(self):
		self.test_transition_released_to_up()
		self.assertEquals(self.button(), Button.State.UP)

	def test_transition_pressed_to_released(self):
		self.test_transition_up_to_pressed()
		self.controller.a = False
		self.assertEquals(self.button(), Button.State.RELEASED)

	def test_transition_released_to_pressed(self):
		self.test_transition_pressed_to_released()
		self.controller.a = True
		self.assertEquals(self.button(), Button.State.PRESSED)

	def test_transition_released_to_pressed_2(self):
		self.test_transition_down_to_released()
		self.controller.a = True
		self.assertEquals(self.button(), Button.State.PRESSED)
