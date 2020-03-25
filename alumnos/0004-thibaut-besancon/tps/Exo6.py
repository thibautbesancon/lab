class Exo():
    def __init__(self):
        self.var = str(input("enter your list\n"))

    def prog(self):
        tab = self.var.split(',')
        tab = list(map(int, tab))
        tab.sort(reverse=True)
        return tab

if __name__ == '__main__':
    n = Exo()
    print(n.prog())