from src.classes.Entity import Entity

class Player(Entity):
		
	def get_weapon(self):
		return self._weapon
		
	def set_weapon(self, weapon_name):
		weapon = self.get_single_item(weapon_name)
		if weapon['type'] != "weapon":
			return f"{weapon.name} is not a weapon"
		else:
			self._weapon = {weapon_name: weapon}
			self.remove_inventory_item(weapon_name)
		
	
	def set_inventory_item(self, item):
		self._inventory.update({item.get_name(): {item.get_description(). item.affect, item.get_apply_to(), item.get_type()}})
		return self._inventory
		
	def remove_inventory_item(self,item_name):
		self._inventory.pop(item_name)
		
		
	
		
