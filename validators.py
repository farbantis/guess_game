import settings


def player_name_validator(player_name: str) -> bool:
    return player_name.replace(' ', '').isalpha()


def player_namelen_validator(player_name: str) -> bool:
    return len(min(player_name.split(), key=len)) >= 3


def choose_and_validate_creature(player: object, action: str) -> None:
    while True:
        print(f'Time to {action}, please choose your character')
        player_creature = int(input(str([f'{x} for {y}' for x, y in settings.GAME_CREATURES.items()])))
        if player_creature in settings.GAME_CREATURES:
            player.creature = player_creature
            break
        print(f'sorry, but character {player_creature} does not exist')


def player_action_validator(player_name: str) -> None:
    while True:
        player_action = input(f'Hi, {player_name}- please type start to begin or help for information.... ')
        if player_action == 'start':
            break
        elif player_action == 'score':
            print('add score display')
        elif player_action == 'help':
            print(settings.RULES)
        elif player_action == 'exit':
            exit()
        else:
            print('your command not recognized, type it again or use help')
