
import settings
from models import Player, Enemy
from game_exceptions import GameOver, EnemyDown
from validators import player_name_validator


def play():
    player_name = input('Enter your name worrier: ')
    if not player_name_validator(player_name=player_name):
        print('please enter the correct name')
        play()
    player_action = input(f'{player_name}, please type start to begin or help.... ')

    player = Player(player_name=player_name)
    level = 1
    enemy = Enemy(level=level)
    enemy.lives = level
    while True:
        print(f'level is {level}')
        # при виникненні винятку EnemyDown підвищує рівень гри на 1, створює новий об'єкт Enemy з новим рівнем
        print('please choose your character')
        player.creature = int(input(str([f'{x} for {y}' for x, y in settings.GAME_CREATURES.items()])))
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            player.score += 5
            level += 1
            enemy = Enemy(level=level)
            print(f'level is {level} now')
        print('===============================================================')

        #Player.defence(enemy_obj=enemy)


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('Your game is over...')
    except KeyboardInterrupt:
        pass
    finally:
        print('Goodbye')

