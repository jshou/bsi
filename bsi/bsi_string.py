class BsiString:
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return '"{}"'.format(self.s)

    def __eq__(self, obj):
        return isinstance(obj, BsiString) and self.s == obj.s
