class Score(object):
    def __init__(self, name, forward, against):
        self.name = name
        self.forward = forward
        self.against = against

    def delta(self):
        return abs(self.forward - self.against)