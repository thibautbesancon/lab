import matplotlib.pyplot as pyplot
class Exo():
    def __init__(self):
        self.var = str(input("enter your list. (list like 1,2,2,3...)\n"))

    def prog(self):
        tab = self.var.split(',')
        list2 = list(dict.fromkeys(tab))
        bin = [0]
        bin = [x - 0.5 for x in range(len(list2) + 1)]
        pyplot.style.use('ggplot')
        pyplot.xlabel('x')
        pyplot.ylabel('y')
        pyplot.title(r'$\mathrm{Histogram\ of\ Exo3}$')
        pyplot.hist(tab, bins=bin, alpha=0.75)
        pyplot.show()

if __name__ == '__main__':
    n = Exo()
    n.prog()



# test iyw : 1,1,2,3,3,5,7,8,9,10,10,11,11,13,13,15,16,17,18,18,18,19,20,21,21,23,24,24,25,25,25,25,26,26,26,27,27,27,27,27,29,30,30,31,33,34,34,34,35,36,36,37,37,38,38,38,40,41,41,42,44,44,45,45,46,47,48,48,49,50,51,52,53,54,55,55,56,57,58,60,61,63,64,65,66,68,70,70,74,74,75,77,77,81,84,84,87,89,90,90,94