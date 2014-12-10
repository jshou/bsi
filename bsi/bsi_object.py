from collections import OrderedDict
from bsi_string import BsiString

class BsiObject:
    def __init__(self):
        self.dict = OrderedDict()

    def set(self, k, v):
        self.dict[k] = v

    def get(self, k):
        return self.dict[k]

    def __str__(self):
        pairs = []

        for pair in self.dict.items():
            key = pair[0]
            if isinstance(pair[1], BsiObject):
                val = pair[1].nested_str()
            else:
                val = str(pair[1])
            pairs.append("{} = {}".format(key, val))
        return '\n'.join(pairs)

    def nested_str(self):
        lines = str(self).split('\n')
        indented_lines = '\n'.join(['\t' + line for line in lines])
        return '{\n' + indented_lines + '\n}'
