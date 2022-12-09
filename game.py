import settings
from models import Player, Enemy
from game_exceptions import GameOver, EnemyDown
from validators import player_name_validator, player_namelen_validator


def play():
    player_name = input('Enter your name worrier: ')
    if not player_namelen_validator(player_name):
        print('your name is too short, must be at least 3 letters')
        play()
    if not player_name_validator(player_name):
        print('only letters and spaces are allowed')
        play()
    player_action = input(f'Hi, {player_name}- please type start to begin or help for information.... ')

    player = Player(player_name=player_name)
    enemy = Enemy(level=settings.STARTING_LEVEL)
    while True:
        print(f'level is {enemy.level}')
        # при виникненні винятку EnemyDown підвищує рівень гри на 1, створює новий об'єкт Enemy з новим рівнем
        try:
            print('')
            print(f'level {enemy.level}, score {player.score}')
            print('please choose your character => validation of input')
            player.creature = int(input(str([f'{x} for {y}' for x, y in settings.GAME_CREATURES.items()])))
            player.attack(enemy)
            print('')

            print('===============================================================')
            print(f'level {enemy.level}, score {player.score}')
            print('please choose your character for defence')
            player.creature = int(input(str([f'{x} for {y}' for x, y in settings.GAME_CREATURES.items()])))
            player.defence(enemy)
            print('===============================================================')

        except EnemyDown:
            player.score += 5
            new_level = enemy.level + 1
            enemy = Enemy(level=new_level)
            print(f'Enemy Down. level is {enemy.level} now, score is {player.score}')


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('Your game is over... your scoure is //')
    except KeyboardInterrupt:
        pass
    finally:
        print('Goodbye')

