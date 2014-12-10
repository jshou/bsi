from bsi_object import BsiObject

class BsiArray:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        items = []
        for i in self.array:
            if isinstance(i, BsiObject):
                items.append(i.nested_str())
            else:
                items.append(str(i))

        return "[ {} ]".format(' '.join(items))

    def __eq__(self, obj):
        return isinstance(obj, BsiArray) and self.array == obj.array
