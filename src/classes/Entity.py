class Entity:
	def __init__(self, _name, _health, _strength, _speed, _agility, _weapon, _inventory):
		self._name = _name # Str
		self._health = _health # Int
		self._strength =_strength # Int
		self._speed = _speed # Int
		self._agility = _agility # Int
		self._weapon = _weapon # Item
		self._inventory = _inventory # Dictanary of Items
	
	def get_name(self):
		return self._name
		
	def get_health(self):
		return self._health
		
	def get_strength(self):
		return self._strength
		
	def get_speed(self):
		return self._speed
		
	def get_agility(self):
		return self._agility
		
	def get_inventory(self):
		return self._inventory
		
	def get_single_item(self, item_name):
		item = self._inventory.get(item_name)
		if item == None:
			raise KeyError("Item not found in inventory") 
		else:
			return {item_name: item}
		
	def set_strength(self, num):
		self._strength = num
		
	def set_speed(self, num):
		self._speed = num
		
	def set_agility(self, num):
		self._agility = num
	
	def set_health(self, num):
		self._health = num
		
	
		
	def take_damage(self, damage):
		# damage = self.attack()
		health = self.get_health()
		health -= damage
		self.set_health(health)
		return self._health
		
	def heal(self, num):
		health = self.get_health()
		health += num
		self.set_health(health)
		return self._health
		
	def use_item(self, item_name):
		item = self.get_single_item(item_name)
		if item.type != "potion":
			return f"{item.name} is not a potion"
		else:
			match item.apply_to:
				case "health":
					self.heal(item.affect)
					return self.get_health()
				case "strength":
					self.set_strength(item.affect + self._strength)
					return self.get_strength()
				case "speed":
					self.set_speed(item.affect + self._speed)
					return self.get_speed()
				case "agility":
					self.set_agility(item.affect + self._agiltiy)
					return self.get_agility()
				case _:
					return "Error: stat not found"
