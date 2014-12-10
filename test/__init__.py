import mox
import unittest

import fplib
from fplib import make_action, ButtonActions, SingleAction, Action, Actions, KeyUp, KeyDown

def l():
	pass

def ll():
	pass

class Test_make_action(unittest.TestCase):
	def test_Action_is_unchanged(self):
		a = Action()
		self.assertEquals(make_action(a), a)

	def test_non_Action_becomes_SingleAction(self):
		self.assertIsInstance(make_action(l), SingleAction)

	def test_non_Action_becomes_SingleAction_with_content(self):
		self.assertEquals(make_action(l).action, l)

	def test_list_becomes_Actions(self):
		self.assertIsInstance(make_action([l, ll]), Actions)

	def test_list_becomes_Actions_with_content(self):
		self.assertEquals(make_action([l, ll]).actions[1], ll)

class TestButtonActions(unittest.TestCase):
	def test_press_non_Action_becomes_Action(self):
		self.assertIsInstance(ButtonActions(l, l).press_action, Action)

	def test_release_non_Action_becomes_Action(self):
		self.assertIsInstance(ButtonActions(l, l).release_action, Action)

	def test_press_non_Action_becomes_Action_with_content(self):
		self.assertEquals(ButtonActions(l, ll).press_action.action, l)

	def test_release_non_Action_becomes_Action_with_content(self):
		self.assertEquals(ButtonActions(l, ll).release_action.action, ll)

	def test_single_non_callable_becomes_KeyDown_KeyUp(self):
		b = ButtonActions('a')
		self.assertIsInstance(b.press_action, KeyDown)
		self.assertEquals(b.press_action.key, 'a')
		self.assertIsInstance(b.release_action, KeyUp)
		self.assertEquals(b.release_action.key, 'a')

class TestActions(mox.MoxTestBase):
	def test_actions_takes_empty_list(self):
		self.assertEquals(Actions([]).actions, [])

	def test_actions_takes_no_args(self):
		self.assertEquals(Actions().actions, [])

	def test_actions_takes_list(self):
		self.assertEquals(Actions([l, ll]).actions[1], ll)

	def test_actions_takes_multiple_args(self):
		self.assertEquals(Actions(l, ll).actions[1], ll)

	def test_actions_takes_1_len_list(self):
		self.assertEquals(Actions([l]).actions[0], l)

	def test_actions_takes_1_action(self):
		self.assertEquals(Actions(l).actions[0], l)

class TestKeyActions(mox.MoxTestBase):
	def setUp(self):
		super(TestKeyActions, self).setUp()
		fplib.keyboard = self.mox.CreateMockAnything()

	def test_KeyDown(self):
		fplib.keyboard.setKeyDown('d')
		self.mox.ReplayAll()
		KeyDown('d')()

	def test_KeyUp(self):
		fplib.keyboard.setKeyUp('u')
		self.mox.ReplayAll()
		KeyUp('u')()
