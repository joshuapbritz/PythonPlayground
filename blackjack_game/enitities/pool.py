class Pool():
    def __init__(self):
        self.bet_value = 0

    def add(self, value):
        self.bet_value = value

    def get(self):
        return self.bet_value * 2
    
    def reset(self):
        self.bet_value = 0
