import datetime as dt


class GameOver(Exception):
    """
    initialize when player looses the game
    records results in a file
    """
    def __init__(self, player: str, score: int):
        self.player = player
        self.score = score
        self.time = dt.datetime.now().strftime("%d/%m/%y %H:%m:%S")
        self.record()

    def record(self):
        """writes game result into a file"""
        with open('score.txt', 'a+', encoding='utf-8') as text_file:
            print(f"{self.player}: {self.score} |{self.time}", file=text_file)


class EnemyDown(Exception):
    """
    left empty
    """
