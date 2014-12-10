class BsiNumber:
    def __init__(self, num):
        self.num = float(num)

    def __eq__(self, obj):
        return isinstance(obj, BsiNumber) and self.num == obj.num

    def __str__(self):
        if self.num.is_integer():
            return str(int(self.num))
        else:
            return str(self.num)
