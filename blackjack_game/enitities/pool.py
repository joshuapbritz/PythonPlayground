class Pool():
    def __init__(self):
        self.bet_value = 0

    def add(self, value):
        self.bet_value = value
    
    def reset(self):
        self.bet_value = 0
