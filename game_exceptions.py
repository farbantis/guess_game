import datetime


class GameOver(Exception):
    """
    В класі має бути реалізований метод для збереження фінального рахунку гри по її завершенню.
    """
    def __init__(self, player, score):
        self.player = player
        self.score = score
        self.time = datetime.datetime.now().strftime("%d/%m/%y %H:%m:%S")
        print('game over launched')
        self.record()

    def record(self):
        with open('score.txt', 'a+') as f:
            print(f"{self.player}: {self.score} |{self.time}")


class EnemyDown(Exception):
    """
    Функціонал не потрібен, тільки декларація.
    """
    print('inside enemy down')
