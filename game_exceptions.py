import datetime


class GameOver(Exception):
    """
    initialize when player looses the game
    records results in a file
    """
    def __init__(self, player: str, score: int):
        self.player = player
        self.score = score
        self.time = datetime.datetime.now().strftime("%d/%m/%y %H:%m:%S")
        self.record()
        print(f'winning score is {self.score}')

    def record(self):
        with open('score.txt', 'a+') as f:
            print(f"{self.player}: {self.score} |{self.time}")


class EnemyDown(Exception):
    """
    left empty
    """

