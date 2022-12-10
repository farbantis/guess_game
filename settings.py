LIVES_AMOUNT = 3
STARTING_LEVEL = 1
HARD_MODE_RATIO = 3
ALLOWED_ATTACKS = [1, 2, 3]
GAME_MODES = ['hard', 'normal']

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
    'show_scores': 'show the score',
    'help': 'show this menu',
    'exit': 'exit the game'
}
