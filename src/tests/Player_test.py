from unittest import TestCase
from src.classes.Player import Player

class PlayerTest(TestCase):

    def test_init(self):
        test = Player("test", 1, 2, 3, 4, {}, {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})

        self.assertEqual(test.get_name(), "test")
        self.assertEqual(test.get_health(), 1)
        self.assertEqual(test.get_strength(), 2)
        self.assertEqual(test.get_speed(), 3)
        self.assertEqual(test.get_agility(), 4)
        self.assertEqual(test.get_inventory(), {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})

    def test_get_weapon(self):
        test = Player("test", 1, 2, 3, 4, {}, {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})

        weapon = test.get_weapon()

        self.assertEqual(weapon, {})

    def test_set_weapon(self):
        test = Player("test", 1, 2, 3, 4, {}, {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})

        with self.assertRaises(KeyError):
            test.set_weapon("P")
        
        test.set_weapon("sword")
        self.assertEqual(test.get_weapon(), {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})
        self.assertEqual(test.get_inventory(), {})

    def test_set_inventory_item(self):
        test = Player("test", 1, 2, 3, 4, {}, {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}})

        test.set_inventory_item({"dagger": {"description": "test dagger", "affect": 1, "apply_to": "strength", "type": "weapon"}})

        self.assertEqual(test.get_inventory(), {"sword": {"description": "test sword", "affect": 2, "apply_to": "strength", "type": "weapon"}, "dagger": {"description": "test dagger", "affect": 1, "apply_to": "strength", "type": "weapon"}})
