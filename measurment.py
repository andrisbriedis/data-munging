class Measurement(object):
    def __init__(self, day, min, max):
        self.day = day
        self.min = min
        self.max = max

    def delta(self):
        return self.max - self.min