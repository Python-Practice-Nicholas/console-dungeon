from Player import Player
from monster import Monster
from Item import Item
from random import randint
import json
import os.path


class Game():

	player = {}
	running = True
	
	
	def start(self):
		while self.running:
			print("Welcome to Dungeon Crawl\n")
			print("------------------")
			print("| 1 - Start New Game |\n")
			print("| 2 - Load Game \t |\n")
			print("| 3 - Exit Game \t |")
			print("------------------\n")
			
			choice = input("Selection (1/2/3): ")
			
			match choice:
				case "1":
					name = input("Enter Player name: ")
					self.player = Player(
					name,
					10,
					randint(1,11),
					randint(1,11),
					randint(1,11),
					Item.create_item("sword"),
					{}
					)
					self.play()
				case "2":
					self.load()
					self.play()
				case "3":
					print("\nThank you for playing!\n")
					self.running = False
				case _:
					print("Invalid selection.\nSelect a new option.")
					
					
	def end(self):
		pass
		
	def save(self):
		is_choosing = True
		
		while is_choosing:
			data = Game.display_file_menu()
			choice = input("Which save file do you wish to use? ")
			match choice:
				case "1" | "save1" | "Save1" | "save 1" | 'Save 1':
					if data["1"] == "empty":
						data["1"] = self.player.player_save_data()
						print(data)
						Game.save_data_to_file(data)
						is_choosing = False
					else:
						choice2 = input("Do you wish to overwrite this save? (y/n)")
						
						if choice2 == "y":
							data["1"] = self.player.player_save_data()
							Game.save_data_to_file(data)
							is_choosing = False
						else:
							pass
				case "2" | "save2" | "Save2" | "save 2" | 'Save 2':
					if data["2"] == "empty":
						data["2"] = self.player.player_save_data()
						Game.save_data_to_file(data)
						is_choosing = False
					else:
						choice2 = input("Do you wish to overwrite this save? (y/n)")
						
						if choice2 == "y":
							data["2"] = self.player.player_save_data()
							Game.save_data_to_file(data)
							is_choosing = False
						else:
							pass
				case "3" | "save3" | "Save3" | "save 3" | 'Save 3':
					if data["3"] == "empty":
						data["3"] = self.player.player_save_data()
						Game.save_data_to_file()
						is_choosing = False
					else:
						choice2 = input("Do you wish to overwrite this save? (y/n)")
						
						if choice2 == "y":
							data["3"] = self.player.player_save_data()
							Game.save_data_to_file(data)
							is_choosing = False
						else:
							pass
				case _:
					print("Invalid selection.\nSelect another option.")
					
					
	def load(self):
		is_choosing = True
		
		while is_choosing:
			data = Game.display_file_menu()
			choice = input("Select a file: ")
			
			match choice:
				case "1" | "save1" | "Save1" | "save 1" | 'Save 1':
					self.player = Player(
					data["1"]["name"],
					data["1"]["health"],
					data["1"]["strength"],
					data["1"]["speed"],
					data["1"]["agility"],
					data["1"]["weapon"],
					data["1"]["inventory"])
					is_choosing = False
				case "2" | "save2" | "Save2" | "save 2" | 'Save 2':
					self.player = Player(
					data["1"]["name"],
					data["1"]["health"],
					data["1"]["strength"],
					data["1"]["speed"],
					data["1"]["agility"],
					data["1"]["weapon"],
					data["1"]["inventory"])
					is_choosing = False
				case "3" | "save3" | "Save3" | "save 3" | 'Save 3':
					self.player = Player(
					data["1"]["name"],
					data["1"]["health"],
					data["1"]["strength"],
					data["1"]["speed"],
					data["1"]["agility"],
					data["1"]["weapon"],
					data["1"]["inventory"])
					is_choosing = False
				case _:
					print("Invalid selection.\nSelect another option.")
					
	def play(self):
		is_playing = True
		
		while is_playing:
			print("\n")
			print("| 1 - Move to next room |\n")
			print("| 2 - Check Stats")
			print("| 3 - Save Game |\n")
			
			choice = input("Selection (1/2/3): ")
			
			match choice:
				case "1":
					print("You walk into the next room")
					self.fight()
					if self.player.get_health() <= 0:
						is_playing = False
				case "2":
					self.player.display_stats()
				case "3":
					self.save()
					is_playing = False
					
					
	def fight(self):
		is_fighting = True
		
		while is_fighting:
			monster = Monster.create_monster()
			
			print(f"You are being attacked by a {monster.get_name()}")
			
			print("-----------------")
			print(f"| 1 - Attack |\n")
			print(f"| 2 - Inventory |\n")
			print(f"| 3 - Run |")
			print("-----------------\n")
			choice = input("Selection: ")
			
			match choice:
				case "1":
					is_fighting = Game.fight_order(monster, self.player)
				case "2":
					print("\nNeeds to be implamented\n")
				case "3":
					if self.player.get_agility() > monster.get_agility():
						print("\nYou have escaped the monster.\n")
						is_fighting = False
					else:
						print("\nYou can't is escape the monster\n")
				case _:
					print("\nInvalid Selection\n")
					
					
					
					
	# class Helper Functions
	@staticmethod
	def display_file_menu():
		saves_path = os.path.relpath("saves/saves.json", "src/classes")
		file = open(saves_path, "r")
		data = json.load(file)
		file.close()
		
		print("-----------------")
		print(f'| Save 1: {data["1"]} |\n')
		print(f'| Save 2: {data["2"]} |\n')
		print(f'| Save 3: {data["3"]} |')
		print("-----------------\n")
		
		return data
		
	@staticmethod
	def save_data_to_file(data):
		saves_path = os.path.relpath("saves/saves.json", "src/classes")
		file = open(saves_path, "w")
		json.dump(data, file, indent=4)
		file.close()
		
	@staticmethod
	def fight_order(monster, player):
		if monster.get_speed() > player.get_speed():
			print(f"{monster.get_name()} attacks first\n")
			monster_damage = monster.attack()
			player.take_damage(monster_damage)
			if Game.check_health(monster, player) == "player-zero":
				print("Player has died")
				return False
			print("------------\n")
			print(f"You attack the {monster.get_name()}\n")
			player_damage = player.attack()
			monster.take_damage(player_damage)
			if Game.check_health(monster, player) == "monster-zero":
				print(f"{player.get_name()} has killed {monster.get_name()}")
				return False
			print("------------\n")
			print(f"Player Health: {player.get_health()}")
			print(f"{monster.get_name()}: {monster.get_health()}")
		else:
			print("Player attacks first\n")
			print(f"You attack the {monster.get_name()}\n")
			player_damage = player.attack()
			monster.take_damage(player_damage)
			if Game.check_health(monster, player) == "monster-zero":
				print(f"{player.get_name()} has killed {monster.get_name()}")
				return False
			print("------------\n")
			print(f"{monster.get_name()} attacks\n")
			monster_damage = monster.attack()
			player.take_damage(monster_damage)
			if Game.check_health(monster, player) == "player-zero":
				print("Player has died")
				return False
			print("------------\n")
			print(f"Player Health: {player.get_health()}")
			print(f"{monster.get_name()}: {monster.get_health()}")
			
		return True
		
	@staticmethod
	def check_health(monster, player):
		if monster.get_health() <= 0:
			return "monster-zero"
			
		if player.get_health() <= 0:
			return "player-zero"
			
		return None
		
		
		
		
		
		
		
g = Game()
g.start()

