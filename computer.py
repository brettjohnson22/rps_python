from player import Player
import random


class Computer(Player):

    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.options)

    def choose_name(self):
        self.name = "EDI"
        print(f"You will be playing {self.name}, an Artificial Intelligence.")
