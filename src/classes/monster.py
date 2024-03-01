from Entity import Entity
import json
import os.path
from random import randint


class Monster(Entity):
	
	@staticmethod
	def create_monster():
		"""Static method to creat a new Monster"""
		monster_path = os.path.relpath("json/monsters.json", "classes")
		names = ["bat"]
		index = randint(0,len(names) - 1)
		print(index)
		name = names[index]
		with open(monster_path) as file:
			data = json.load(file)
			monster_data = data[name]
			health = monster_data["health"]
			strength = monster_data["strength"]
			speed = monster_data["speed"]
			agility = monster_data["agility"]
			weapon = monster_data["weapon"]
			inventory = monster_data["inventory"]
			
			monster = Monster(name, health, strength, speed, agility, weapon, inventory)
			return monster
	
	def get_weapon(self):
		return self._weapon

	def attack(self):
		strength = self.get_strength()
		weapon = self.get_weapon()

		return strength + weapon["affect"]

	
			
