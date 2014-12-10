from collections import OrderedDict

class BsiObject:
    def __init__(self):
        self.dict = OrderedDict()

    def add(self, k, v):
        self.dict[k] = v

    def get(self, k):
        return self.dict[k]

    def __str__(self):
        pairs = ["{} = {}".format(pair[0], pair[1]) for pair in self.dict.items()]
        return '\n'.join(pairs)
