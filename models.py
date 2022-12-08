from random import randint
import settings
from game_exceptions import EnemyDown, GameOver


class Enemy:
    lives = 1

    def __init__(self, level):
        self.level = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decreased_lives(self, lives):
        lives -= 1
        if lives < 0:
            EnemyDown()


class Player:
    score = 0
    lives = settings.LIVES_AMOUNT

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def fight(attack, defence):
        # returns the result of an attack or defence
        # 0 draw, 1 success, -1 fault
        return

    def decrease_lives(self):
        GameOver()

    def attack(self, enemy_obj):
        pass

    def defence(self, enemy_obj):
        pass

"""
отримує input (1, 2, 3) від користувача;
обирає атаку противника з об'екту enemy_obj;
викликає метод fight();
Якщо результат 0 - вивести "It's a draw!"
Якщо 1 = "You attacked successfully!" та зменшує кількість життів противника на 1;
Якщо -1 = "You missed!"
defence(self, enemy_obj) - такий самий, як метод attack(), тільки в метод fight першим передається атака противника, та при вдалій атаці противника викликається метод decrease_lives гравця.
    """




