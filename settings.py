GAME_MODES = {
    'hard': 3,
    'normal': 1
}

GAME_CREATURES = (
    (1, 'MAGICIAN'),
    (2, 'WORRIER'),
    (3, 'HIGHWAYMAN')
)
PLAYER_GAME_RESULT = {
    0: "It's a draw",
    1: 'You attacked successfully!',
    -1: 'You missed'
}
ENEMY_GAME_RESULT = {
    0: "It's a draw",
    1: 'Enemy attacked successfully!',
    -1: 'Enemy missed'
}
RULES = {
    'start': 'start the game',
    'show_scores': 'shows top 10 players',
    'help': 'show this menu',
    'exit': 'exit the game'
}
LIVES_AMOUNT = 3
STARTING_LEVEL = 1
ALLOWED_ATTACKS = [x[0] for x in GAME_CREATURES]
MIN_PLAYER_NAME_LEN = 3
MAX_PLAYER_NAME_LEN = 15
