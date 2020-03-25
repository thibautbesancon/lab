# En matemáticas, la secuencia de Fibonacci es una secuencia
# de números enteros en la que cada término es la suma de los
# dos anteriores. Comienza con los términos 0 y 1
# Este programa muestra los 10 principales números de fibonacci
# La forma de este programa es un programa recursivo

def fibo (n, a = 0, b = 1):         # funcion de fibonacci
   while n != 0:                    # el bucle while para empezar en 10 y terminar en 0
      return fibo (n-1, b, a + b)   # return otros números de fibonacci
   return a                         # return a = 0

for i in range (0,10):              # Main, bucle de 0 a 10
   print (fibo (i))                 # print numero de fibonacci