class BsiArray:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        items = ' '.join([str(i) for i in self.array])
        return "[ {} ]".format(items)

    def __eq__(self, obj):
        return isinstance(obj, BsiArray) and self.array == obj.array
