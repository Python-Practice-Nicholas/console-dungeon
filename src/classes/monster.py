from Entity import Entity
import json


class Monster(Entity):
	
	@staticmethod
	def create_monster(name):
		"""Static method to creat a new Monster"""
		with open('../json/monsters.json') as file:
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
			
