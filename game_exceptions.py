import datetime as dt
import settings


class GameOver(Exception):
    """
    initialize when player looses the game
    records results in a file
    """
    def __init__(self, player: str, score: int, game_mode: int):
        self.player = player
        self.score = score
        self.time = dt.datetime.now().strftime("%d/%m/%Y %H:%m:%S")
        self.game_mode = game_mode
        self.record()

    def record(self):
        """writes game result into a file"""
        with open('scores.txt', 'a+', encoding='utf-8') as text_file:
            mode_dict = {y: x for x, y in settings.GAME_MODES.items()}
            print(f"{self.player}{' ' * (settings.MAX_PLAYER_NAME_LEN-len(self.player))}:"
                  f" {self.score}{' ' * (3 - len(str(self.score)))} | "
                  f"{self.time} ({mode_dict[self.game_mode][0].upper()})",
                  file=text_file)


class EnemyDown(Exception):
    """
    left empty
    """
