import time
import random

moves = ['rock', 'paper', 'scissors']


class Player:
    score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def __init__(self):
        Player.__init__(self)

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def __init__(self):
        self.choice = ""
        self.choices = ['rock', 'paper', 'scissors']

    def move(self):
        self.choice = ""
        while self.choice not in self.choices:
            self.choice = input("Choose Now! rock,"
                                "paper, scissors? : ").lower()
        return self.choice


class ReflectPlayer(Player):

    def __init__(self):
        self.reflect = random.choice(moves)

    def move(self):
        return self.reflect

    def learn(self, my_move, their_move):
        self.reflect = their_move


class CyclePlayer(ReflectPlayer):

    def learn(self, my_move, their_move):
        self.reflect = moves[(moves.index(my_move) + 1) % 3]


def print_time(message, pause=1):
    print(message)
    time.sleep(pause)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("player 1 wins this round")
            self.p1.score += 1
        elif beats(move2, move1):
            print("player 2 wins this round")
            self.p2.score += 1
        else:
            print("A Tie!")
        print(f"Scores: Player 1: {self.p1.score} Player 2:{self.p2.score}")

    def play_game(self):
        print_time("Welcome User!")
        print_time("The evil Decepticons have invaded your planet.")
        print_time("To save Humanity you must 'WIN' best out of 3 rounds.")
        print_time("If the game ends in a 'TIE' you lose")
        print_time("The game is rock, paper, scissors")
        print_time("GOOD LUCK!!\n")
        print_time("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

        if self.p1.score > self.p2.score:
            print("Player 1 Wins the Game!")
        elif self.p2.score > self.p1.score:
            print("Player 2 Wins the Game!")
        else:
            print("You lose! You must WIN to save your planet!!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
