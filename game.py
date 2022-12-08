from models import Player, Enemy
from game_exceptions import GameOver


def play():
    payer_name = input('Enter your name worrier: ')
    player = Player(player_name=payer_name)
    level = 1
    enemy = Enemy(level)
    while True:
        # при виникненні винятку EnemyDown підвищує рівень гри на 1, створює новий об'єкт Enemy з новим рівнем
        Player.attack(enemy_obj=enemy)
        Player.defence(enemy_obj=enemy)


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('Your game is over...')
        # record results into a table
    except KeyboardInterrupt:
        pass
    finally:
        print('Goodbye')

