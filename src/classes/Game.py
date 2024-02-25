from Player import Player
from monster import Monster
from Item import Item
import json
import os

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
                    pass
                case "2":
                    self.load()
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
                    self.player = Player(data["1"])
                    is_choosing = False
                case "2" | "save2" | "Save2" | "save 2" | 'Save 2':
                    self.player = Player(data["2"])
                    is_choosing = False
                case "3" | "save3" | "Save3" | "save 3" | 'Save 3':
                    self.player = Player(data["3"])
                    is_choosing = False
                case _:
                    print("Invalid selection.\nSelect another option.")
            
    def play(self):
        is_playing = True

        while is_playing:
            print("| 1 - Move to next room |\n")
            print("| 2 - Check Stats")
            print("| 3 - Save Game |\n")

            choice = input("Selection (1/2/3): ")

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

        return data
    
    @staticmethod
    def save_data_to_file(data):
        file = open("saves/saves.json", "w")
        json.dump(data, file)
        file.close()

    @staticmethod
    def fight():
        pass




g = Game()
g.start()
