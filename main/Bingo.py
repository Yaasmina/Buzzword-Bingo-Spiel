import random
import time

class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.card = [["" for _ in range(5)] for _ in range(5)]

    def generate_bingo_card(self, words):
        used_indices = set()
        for i in range(5):
            for j in range(5):
                index = random.choice([k for k in range(len(words)) if k not in used_indices])
                used_indices.add(index)
                self.card[i][j] = words[index]

    def display_bingo_card(self):
        for row in self.card:
            print("\t".join(row))
        print("\n")

    def mark_bingo_card(self, word):
        for i in range(5):
            for j in range(5):
                if self.card[i][j] == word:
                    self.card[i][j] = "X"
                    return True
        return False

    def check_winner(self):
        # Check rows and columns
        for i in range(5):
            if all(self.card[i][j] == "X" for j in range(5)) or all(self.card[j][i] == "X" for j in range(5)):
                return True
        # Check diagonals
        if all(self.card[i][i] == "X" for i in range(5)) or all(self.card[i][4-i] == "X" for i in range(5)):
            return True
        return False

def log_game_event(filename, event):
    with open(filename, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d-%H-%M-%S')} {event}\n")
