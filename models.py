from random import randint
import settings
from game_exceptions import EnemyDown, GameOver


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decreased_lives(self):
        print(f'decresing enemy live, was {self.lives} is {self.lives -1}')
        self.lives -= 1
        if self.lives <= 0:
            EnemyDown()


class Player:
    # Атрибути: name, lives, score, allowed_attacks
    def __init__(self, player_name):
        self.player_name = player_name
        self.lives = settings.LIVES_AMOUNT
        self.score = 0

    @staticmethod
    def fight(attack=None, defence=None) -> 0 or -1 or 1:
        if attack == defence:
            return 0
        elif attack + 1 == defence or attack - 2 == defence:
            return 1
        return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            GameOver(self.player_name, self.score)

    def attack(self, enemy_obj):
        player_move = self.creature
        print(f'player move {player_move}')
        enemy_move = enemy_obj.select_attack() # обирає атаку противника з об'екту enemy_obj;
        print(f'enemy move {enemy_move}')
        result = self.fight(player_move, enemy_move)
        if result == 0:
            print("It's a draw")
        elif result == 1:
            print('You attacked successfully!')
            self.score += 1
            enemy_obj.decreased_lives()
        elif result == -1:
            print('You missed, and lost a live')
            self.decrease_lives()
        print(f'your lives: {self.lives} | enemy lives: {enemy_obj.lives}')

    def defence(self, enemy_obj):
        enemy_move = enemy_obj.select_attack()  # обирає атаку противника з об'екту enemy_obj;
        print(f'enemy move {enemy_move}')
        player_move = self.creature
        print(f'player move {player_move}')
        result = self.fight(enemy_move, player_move)
        if result == 0:
            print("It's a draw")
        elif result == 1:
            print('Enemy attacked successfully!')
            self.decrease_lives()
        elif result == -1:
            print('Enemy missed')
        print(f'your lives: {self.lives} | enemy lives: {enemy_obj.lives}')






