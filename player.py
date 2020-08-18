class Player:
    def __init__(self, name):
        self.score = 0
        self.options = ["rock", "paper", "scissors"]
        self.chosen_gesture = ""
        self.name = name

    def choose_gesture(self):
        self.chosen_gesture = input(f"{self.name}, choose rock, paper, or scissors: ")

    def choose_name(self):
        self.name = input(f"What is your name, {self.name}? ")