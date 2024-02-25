from Entity import Entity
from Item import Item

class Player(Entity):
		
	def get_weapon(self):
		"""Returns the Player's Weapon"""
		return self._weapon
		
	def set_weapon(self, weapon_name):
		"""Sets the player's current weapon"""
		weapon = self.get_single_item(weapon_name)
		if weapon['type'] != "weapon":
			return f"{weapon.name} is not a weapon"
		else:
			self._weapon = {weapon_name: weapon}
			self.remove_inventory_item(weapon_name)
		
	
	def set_inventory_item(self, item):
		"""Adds an item to the Player's inventory"""
		self._inventory.update(
			{
				item.get_name(): 
				{
					"description": item.get_description(), 
					"affect": item.get_affect(), 
					"apply_to": item.get_apply_to(), 
					"type": item.get_type()
				}
			})
		return self._inventory
		
	def remove_inventory_item(self,item_name):
		"""Removes an item from the Player's inventory"""
		self._inventory.pop(item_name)

	def display_stats(self):
		"""Displays the Player's current stats"""
		print(f"Player: {self.get_name()}")
		print(f"Health: {self.get_health()}")
		print(f"Strength: {self.get_strength()}")
		print(f"Agelity: {self.get_agility()}")
		print(f"Speed: {self.get_speed()}")

	def player_save_data(self):
		"""Returns the Player's information in a savable format"""
		return {
			"name": self.get_name(), 
			"Health": self.get_health(), 
			"strength": self.get_strength(), 
			"speed": self.get_speed(), 
			"agility": self.get_agility(), 
			"weapon": self.get_weapon(),
			"inventory": self.get_inventory()
			}
