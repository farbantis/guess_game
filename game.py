import settings
from models import Player, Enemy
from game_exceptions import GameOver, EnemyDown
from validators import player_name_validator, player_namelen_validator, choose_and_validate_creature, \
    player_action_validator


def play():
    player_name = input('Enter your name worrier: ')
    if not player_namelen_validator(player_name):
        print('your name is too short, must be at least 3 letters')
        play()
    if not player_name_validator(player_name):
        print('only letters and spaces are allowed')
        play()
    player_action_validator(player_name)
    player = Player(player_name=player_name)
    enemy = Enemy(level=settings.STARTING_LEVEL)
    print(f"{'*' * 5} get ready to rumble {'*' * 5}")
    while True:
        try:
            print(f'level {enemy.level}, score {player.score}')
            choose_and_validate_creature(player, 'attack')
            player.attack(enemy)
            print('')

            print(f'level {enemy.level}, score {player.score}')
            choose_and_validate_creature(player, 'defence')
            player.defence(enemy)
            print('')

        except EnemyDown:
            player.score += 5
            new_level = enemy.level + 1
            enemy = Enemy(level=new_level)
            print(
                f"{'*' * 5}"
                f" Enemy terminated, welcome to level {enemy.level}, so far you got {player.score} points {'*' * 5}")


if __name__ == '__main__':
    try:
        play()
    except GameOver as gm_ov:
        print(f'Your game is over, you managed to get {gm_ov.args[1]} points')
    except KeyboardInterrupt:
        pass
    finally:
        print('Goodbye')
