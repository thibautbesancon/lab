class Exo():
    def __init__(self):
        self.var = int(input("number ?\n"))
        self.var2 = int(input("time ?\n"))

    def add(self):
        temp = 1
        result = 0
        while 1 :
            if self.var2 == 0:
                print(result)
                return result
            else:
                result += self.var * self.var2 * temp
                temp *= 10
                self.var2 -= 1

if __name__ == '__main__':
    n = Exo()
    n.add()
