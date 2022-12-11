from random import randint
from settings import ALLOWED_ATTACKS, LIVES_AMOUNT, PLAYER_GAME_RESULT, ENEMY_GAME_RESULT
from game_exceptions import EnemyDown, GameOver


class Enemy:
    """class represents enemy"""
    def __init__(self, level: int, game_mode: int):
        self.level = level
        self.lives = level * game_mode

    @staticmethod
    def select_attack():
        """selects random attack between 1 and 3"""
        return randint(1, 3)

    def decreased_lives(self):
        """decreases enemy life"""
        self.lives -= 1
        if self.lives <= 0:
            raise EnemyDown()


class Player:
    """class represents player"""
    def __init__(self, player_name: str, game_mode: int):
        self.player_name = player_name
        self.lives = LIVES_AMOUNT
        self.score = 0
        self.allowed_attacks = ALLOWED_ATTACKS
        self.creature = None
        self.game_mode = game_mode

    @staticmethod
    def fight(attack: int, defence: int) -> 0 or -1 or 1:
        """determines the winner of the fight"""
        if attack == defence:
            return 0
        if defence in [attack + 1, attack - 2]:
            return 1
        return -1

    def decrease_lives(self):
        """decreased player's life"""
        self.lives -= 1
        if self.lives <= 0:
            raise GameOver(self.player_name, self.score, self.game_mode)

    def attack(self, enemy_obj):
        """player's attack mode"""
        result = self.fight(self.creature, enemy_obj.select_attack())
        print(PLAYER_GAME_RESULT[result])
        if result == 1:
            self.score += 1 * self.game_mode
            enemy_obj.decreased_lives()
        print(f'your lives: {self.lives} | enemy lives: {enemy_obj.lives}\n')

    def defence(self, enemy_obj):
        """player's defence mode"""
        result = self.fight(enemy_obj.select_attack(), self.creature)
        print(ENEMY_GAME_RESULT[result])
        if result == 1:
            self.decrease_lives()
        print(f'your lives: {self.lives} | enemy lives: {enemy_obj.lives}\n')
