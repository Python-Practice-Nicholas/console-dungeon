from Player import Player
from monster import Monster
from Item import Item
import json
import os

class Game():
    
    player = {}

    def start(self):
        pass

    def end(self):
        pass

    def save(self):
        Game.display_file_menu()
        choice = input("Which save file do you wish to use? ")
        match choice:
            case "1" | "save1" | "Save1" | "save 1" | 'Save 1':
                if data["1"] == "empty":
                    data["1"] = self.player
                    Game.save_data_to_file()
                else:
                    choice2 = input("Do you wish to overwrite this save? (y/n)")

                    if choice2 == "y":
                        data["1"] = self.player
                        Game.save_data_to_file()
                    else:
                        pass
            case "2" | "save2" | "Save2" | "save 2" | 'Save 2':
                if data["2"] == "empty":
                    data["2"] = self.player
                    Game.save_data_to_file()
                else:
                    choice2 = input("Do you wish to overwrite this save? (y/n)")

                    if choice2 == "y":
                        data["2"] = self.player
                        Game.save_data_to_file()
                    else:
                        pass
            case "3" | "save3" | "Save3" | "save 3" | 'Save 3':
                if data["3"] == "empty":
                    data["3"] = self.player
                    Game.save_data_to_file()
                else:
                    choice2 = input("Do you wish to overwrite this save? (y/n)")

                    if choice2 == "y":
                        data["3"] = self.player
                        Game.save_data_to_file()
                    else:
                        pass
    def load(self):
        Game.display_file_menu()
        choice = input("Select a file: ")
        
        match choice:
            case "1" | "save1" | "Save1" | "save 1" | 'Save 1':
            	self.player = data["1"]
            case "2" | "save2" | "Save2" | "save 2" | 'Save 2':
            	self.player = data["2"]
            case "3" | "save3" | "Save3" | "save 3" | 'Save 3':
            	self.player = data["3"]
            	
    # class Helper Functions
    
    @staticmethod
    def display_file_menu():
    	file = open("saves/saves.json", "r")
    	data = json.load(file)
    	file.close()
    	
    	print("-----------------")
    	print(f"| Save 1: {data["1"]} |\n")
    	print(f"| Save 2: {data["2"]} |\n")
    	print(f"| Save 3: {data["3"]} |")
    	print("-----------------\n")
    
    @staticmethod
    def save_data_to_file():
    	file = open("saves/saves.json", "w")
      json.dump(data, file)
      file.close()




g = Game()
g.player = {"name": "second TEST"}
g.save()
