def player_name_validator(player_name: str) -> bool:
    return player_name.replace(' ', '').isalpha()


def player_namelen_validator(player_name: str) -> bool:
    return len(min(player_name.split(), key=len)) >= 3


