class Score:
    score = 0

    def __init__(self):
        self.score = 0

    def plus(self, n):
        self.score += n

    def minus(self, n):
        self.score -= n