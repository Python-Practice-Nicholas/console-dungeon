from Entity import Entity
from unittest import TestCase

class EntityTests(TestCase):
	
	def test_init(self):
		test = Entity("test", 1, 2, 3, 4, {"name":"sword", "description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}, {})
		
		self.assertEqual(test.name, "test")
		self.assertEqual(test.health, 1)
		self.assertEqual(test.strength, 2)
		self.assertEqual(test.speed, 3)
		self.assertEqual(test.agility, 4)
		self.assertEqual(test.weapon, {"name":"sword", "description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"})
		self.assertEqual(test.inventory, {})
