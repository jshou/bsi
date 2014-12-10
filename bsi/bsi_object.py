class BsiObject:
    def __init__(self):
        self.dict = {}

    def add(self, k, v):
        self.dict[k] = v

    def get(self, k):
        return self.dict[k]
