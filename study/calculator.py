class Calc :
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreCalc(Calc) :
    def pow(self):
        result = self.first**self.second
        return result

class SafeCalc(MoreCalc) :
    def div(self):
        if self.second == 0:
            return "error"
        else:
            return self.first / self.second

a = SafeCalc(4,0)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())