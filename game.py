from player import Player
from human import Human
from computer import Computer


class Game:

    def __init__(self):
        self.player_one = Human("Player One")
        self.player_two = Player("Player Two")

    def welcome(self):
        print("Welcome to the game!")

    def game_mode(self):
        response = input("Do you want a one player or two player game? Type '1' or '2': ")
        if response == "1":
            self.player_two = Computer("Player Two")
        elif response == "2":
            self.player_two = Human("Player Two")
        else:
            self.game_mode()

    def get_names(self):
        self.player_one.choose_name()
        self.player_two.choose_name()

    def compare_gestures(self):
        print(f"{self.player_one.name} throws {self.player_one.chosen_gesture}\n{self.player_two.name} throws {self.player_two.chosen_gesture}")
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("Tie round!")
        elif (self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "scissors") or (
                self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture == "rock") or (
                self.player_one.chosen_gesture == "scissors" and self.player_two.chosen_gesture == "paper"):
            self.player_one.score += 1
            print(f"{self.player_one.name} wins this round!")
        else:
            self.player_two.score += 1
            print(f"{self.player_two.name} wins this round!")

    def display_winner(self):
        if self.player_one.score == 3:
            print(f"{self.player_one.name} wins the game!")
        else:
            print(f"{self.player_two.name} wins the game!")

    def run_game(self):
        self.welcome()
        self.game_mode()
        self.get_names()
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.compare_gestures()
        self.display_winner()
