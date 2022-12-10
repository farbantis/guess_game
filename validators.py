import sys
from settings import GAME_CREATURES, RULES, GAME_MODES


def game_mode_choose_and_validate():
    """select and validate game mode"""
    while True:
        game_mode = input('type "hard" or "normal" for gamemode: ')
        if game_mode.lower() in GAME_MODES:
            return game_mode
        print(f'sorry, but {game_mode} does not exist, try again')


def player_name_validator(player_name: str) -> bool:
    """checks if player's  name consists of letters and spaces"""
    return player_name.replace(' ', '').isalpha()


def player_namelen_validator(player_name: str) -> bool:
    """check player's name - should have at least 3 letters"""
    return len(min(player_name.split(), key=len)) >= 3


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
        print(f'sorry, but character {player_creature} does not exist')


def player_action_and_validator(player_name: str) -> None:
    """main menu"""
    while True:
        player_action = input(f'Hi, {player_name}- please type start to begin or help for information ')
        if player_action == 'start':
            break
        if player_action == 'show_scores':
            with open('score.txt', encoding='utf-8') as file:
                data = file.readlines()
                data.sort(key=lambda x: int(x.split()[-3]), reverse=True)
                for index, data in enumerate(data[:11], 1):
                    print(index, data, end='')
        elif player_action == 'help':
            print(RULES)
        elif player_action == 'exit':
            sys.exit('interrupted by user')
        else:
            print('your command not recognized, type it again or use help')
