import sys
import settings
from settings import GAME_CREATURES, RULES, GAME_MODES, MIN_PLAYER_NAME_LEN, MAX_PLAYER_NAME_LEN


def game_mode_choose_and_validate():
    """select and validate game mode"""
    while True:
        game_mode = input('type "hard" or "normal" for game mode: ').lower()
        if game_mode in GAME_MODES:
            return GAME_MODES[game_mode]
        print(f"{' ' * 4} sorry, but {game_mode} does not exist, try again")


def player_name_input():
    """picks up player's name and it's validation"""
    while True:
        player_name = input('Enter your name worrier: ')
        if not player_min_name_len_validator(player_name):
            print(f"{' ' * 4}your name is too short, must be at least {MIN_PLAYER_NAME_LEN} letters")
        elif not player_max_name_len_validator(player_name):
            print(f"{' ' * 4}your name is too long, must less than {MAX_PLAYER_NAME_LEN} letters")
        elif not player_name_validator(player_name):
            print('only letters and spaces are allowed')
        else:
            return ' '.join([x.capitalize() for x in player_name.split()])


def player_name_validator(player_name: str) -> bool:
    """checks if player's  name consists of letters and spaces"""
    return player_name.replace(' ', '').isalpha()


def player_min_name_len_validator(player_name: str) -> bool:
    """check player's name"""
    return len(min(player_name.split(), key=len)) >= 3


def player_max_name_len_validator(player_name: str) -> bool:
    """check player's name len"""
    return len(player_name) < settings.MAX_PLAYER_NAME_LEN


def choose_and_validate_creature(player: object, action: str) -> None:
    """accepts players choice of allowed characters"""
    while True:
        print(f'Time to {action}, please choose your character')
        player_creature = input(''.join([f"{x[0]} for {x[1]}, " for x in GAME_CREATURES])[:-2] + ': ')
        if player_creature.isdigit():
            player_creature = int(player_creature)
            if player_creature in player.allowed_attacks:
                player.creature = player_creature
                break
        print(f"{' ' * 4} sorry, but character {player_creature} does not exist")


def player_menu_and_validator(player_name: str) -> None:
    """main menu"""
    print(f"Hi, {player_name} {'*' * 5}")
    while True:
        player_action = input('please type "start" to begin or "help" for information ')
        if player_action == 'start':
            break
        if player_action == 'show_scores':
            with open('scores.txt', encoding='utf-8') as file:
                data = file.readlines()
                data.sort(key=lambda x: int(x.split()[-5]), reverse=True)
                for index, data in enumerate(data[:10], 1):
                    print(f"{index}. {data}", end='')
        elif player_action == 'help':
            print((''.join([f"{' ' * 4}{x}: {y}\n" for x, y in RULES.items()])[:-2]))
        elif player_action == 'exit':
            sys.exit('interrupted by user')
        else:
            print(f"{' ' * 4}your command not recognized, type it again or use help")
