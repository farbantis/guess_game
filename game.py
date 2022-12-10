from settings import STARTING_LEVEL
from models import Player, Enemy
from game_exceptions import GameOver, EnemyDown
from validators import player_name_input, choose_and_validate_creature,\
    player_menu_and_validator, game_mode_choose_and_validate


def play():
    """creates player, enemy and launches attack and defence"""
    game_mode = game_mode_choose_and_validate()
    player_name = player_name_input()
    player_menu_and_validator(player_name)
    player = Player(player_name=player_name, game_mode=game_mode)
    enemy = Enemy(level=STARTING_LEVEL, game_mode=game_mode)
    print(f"{'*' * 5} get ready to rumble {'*' * 5}\n")
    while True:
        try:
            choose_and_validate_creature(player, 'attack')
            player.attack(enemy)

            choose_and_validate_creature(player, 'defence')
            player.defence(enemy)

        except EnemyDown:
            player.score += 5 * player.game_mode
            enemy = Enemy(level=enemy.level + 1, game_mode=game_mode)
            print(
                f"{'*' * 5}"
                f" Enemy terminated, welcome to level {enemy.level},"
                f" so far you got {player.score} points {'*' * 5}\n")


if __name__ == '__main__':
    try:
        play()
    except GameOver as gm_ov:
        print(f'Your game is over, you managed to get {gm_ov.args[1]} points')
    except KeyboardInterrupt:
        pass
    finally:
        print('Goodbye')
