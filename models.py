from random import randint
import settings
from game_exceptions import EnemyDown, GameOver



class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = 1

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decreased_lives(self):
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
            GameOver()

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
            # level += 1
            enemy_obj.decreased_lives()
        elif result == -1:
            print('You miseed')
        print(f'lives are {self.lives}')


    def defence(self, enemy_obj):
        pass

"""
defence(self, enemy_obj) - такий самий, як метод attack(), тільки в метод fight
 першим передається атака противника, та при вдалій атаці противника викликається метод 
 decrease_lives гравця.
    """




