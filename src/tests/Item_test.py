from src.classes.Item import Item
from unittest import TestCase


class ItemTests(TestCase):
	
	def test_init(self):
		item = Item("test", "test item", 2, "speed", "potion")
		
		self.assertEqual(item.get_name(), "test")
		self.assertEqual(item.get_description(), "test item")
		self.assertEqual(item.get_affect(), 2)
		self.assertEqual(item.get_apply_to(), "speed")
		self.assertEqual(item.get_type(), "potion")
	
