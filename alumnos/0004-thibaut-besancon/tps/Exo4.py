import matplotlib.pyplot as pyplot

file=open("Values","r")
tab = file.readlines()
list2 = list(dict.fromkeys(tab))
bin = [0]
bin = [x - 0.5 for x in range(len(list2) + 1)]
pyplot.style.use('ggplot')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.title(r'$\mathrm{Histogram\ of\ Exo4}$')
pyplot.hist(tab, bins=bin, alpha=0.75)
pyplot.show()