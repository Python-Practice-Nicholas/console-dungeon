class Entity:
	self._name
	self._health
	self._strength
	self._speed
	self._agility
	self._weapon
	self._inventory
	
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
		
	def set_strength(self, num):
		self._strength = num
		
	def set_speed(self, num):
		self._speed = num
		
	def set_agility(self, num):
		self._agility = num
		
	def attack(self):
		return self._strength + weapon._affect
		
	def take_damage(self):
		damage = self.attack()
		self._health - damage
		return self._health
		
	def heal(self, num):
		self._health = self._health + num
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
