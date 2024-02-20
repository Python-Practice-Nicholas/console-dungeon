from src.classes.Entity import Entity
from unittest import TestCase

class EntityTests(TestCase):
	
	def test_init(self):
		test = Entity("test", 1, 2, 3, 4, {}, {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})
		
		self.assertEqual(test.get_name(), "test")
		self.assertEqual(test.get_health(), 1)
		self.assertEqual(test.get_strength(), 2)
		self.assertEqual(test.get_speed(), 3)
		self.assertEqual(test.get_agility(), 4)
		self.assertEqual(test.get_inventory(), {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})

	def test_get_single_item(self):
		test = Entity("test", 1, 2, 3, 4, {}, {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})
		item = test.get_single_item("sword")

		self.assertEqual(item, {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"})

	def test_set_funcs(self):
		test = Entity("test", 1, 2, 3, 4, {}, {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})

		test.set_strength(10)
		test.set_speed(11)
		test.set_agility(12)

		self.assertEqual(test.get_strength(), 10)
		self.assertEqual(test.get_speed(), 11)
		self.assertEqual(test.get_agility(), 12)

	def test_take_damage(self):
		test = Entity("test", 1, 2, 3, 4, {}, {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})

		test.take_damage(1)

		self.assertEqual(test.get_health(), 0)

	def test_heal(self):
		test = Entity("test", 1, 2, 3, 4, {}, {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})

		test.heal(9)

		self.assertEqual(test.get_health(), 10)