# coding:utf-8
import multiprocessing
import time
import argparse

##Hola, no pude usar tus fotos.
##De hecho, sus imágenes están en formato ANSI. 
##Trabajando mayormente con utf-8, no sabía cómo usar tus imágenes.
##Por eso, me creé un archivo ppm usando el mismo método para trabajar
##en el proyecto. Encontrarán adjunto el programa en c que usé para hacer mi imagen.

def takeppm(filename): ##Take e ppm file, cut the header and the body in 2 string documents
    ##open the file
    fic = open(filename, 'r')
    ##take the header
    temp = fic.readlines(25)
    header = temp[0] + temp[1] + temp[2] + temp[3]
    ##take the body
    body = fic.read()
    ##close the file
    fic.close()
    return (header, body)

##It's the 3 same function
def process_red(header, body):
    ##split the body to get a list
    bodyred = body.split()
    i = 0
    ##To change all value != red to a 0
    for value in bodyred:
        ##If the value is not for the red
        if (i % 3) != 0:
            bodyred[i] = 0
        i += 1
    ##To Know the number of pixel in a column 
    imagered = header
    temp = header.split()
    numbpix = int(temp[4])

    i = 0
    ##Here it's to reformat the file with the new value
    for value in bodyred:
        imagered += str(value) + " "
        ##if it's the end of the column
        if i == 3 * numbpix - 1:
            imagered += "\n"
            i = 0
        else:
            i += 1
    ##open/create a file to stock the new image
    f = open("1-red.ppm", "w")
    f.write(imagered)
    f.close()

def process_green(header, body):
    bodygreen = body.split()
    i = 0
    ##To change all value != green to a 0
    for value in bodygreen:
        ##If the value is not for the green
        if (i % 3) != 1:
            bodygreen[i] = 0
        i += 1
    imagegreen = header
    temp = header.split()
    numbpix = int(temp[4])
    i = 0
    for value in bodygreen:
        imagegreen += str(value) + " "
        if i == 3 * numbpix - 1:
            imagegreen += "\n"
            i = 0
        else:
            i += 1
    f = open("2-green.ppm", "w")
    f.write(imagegreen)
    f.close()

def process_blue(header, body):
    bodyblue = body.split()
    i = 0
    ##To change all value != blue to a 0
    for value in bodyblue:
        ##If the value is not for the blue
        if (i % 3) != 2:
            bodyblue[i] = 0
        i += 1
    imageblue = header
    temp = header.split()
    numbpix = int(temp[4])
    i=0
    for value in bodyblue:
        imageblue += str(value)+" "
        if i == 3*numbpix-1:
            imageblue += "\n"
            i=0
        else:
            i+=1
    f = open("3-blue.ppm", "w")
    f.write(imageblue)
    f.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Abrir y leer un documento")
    parser.add_argument("-r", "--red", default=1, help="Escala para rojo")
    parser.add_argument("-g", "--green", default=1, help=" Escala para verde")
    parser.add_argument("-b", "--blue", default=1, help="Escala para azul")
    parser.add_argument("-s", "--size", default=1024, help="Bloque de lectura")
    parser.add_argument("-f", "--file", default="image.ppm", help="Archivo a procesar")
    
    args = parser.parse_args()

    if args.red < 0 or args.blue < 0 or args.green < 0:
        print("El color no puede tener un valor negativo")
        sys.exit()
    if args.size < 0:
        print("El tamaño de los datos no puede ser negativo")
        sys.exit()
    try:
        doc = open(args.file, "rb")

    except FileNotFoundError:
        print("El documento no está en la carpeta")
        sys.exit()

    ##Take a filename ppm and cut the header and the body
    header, body = takeppm(args.file)

    ##Creation of  the 3 process in different processor
    if args.blue == 1:
        prB = multiprocessing.Process(target=process_blue(header, body))
    if args.red == 1:
        prR = multiprocessing.Process(target=process_red(header, body))
    if args.green == 1:
        prG = multiprocessing.Process(target=process_green(header, body))
   

    ##Start the process 
    prB.start()
    prR.start()
    prG.start()

    ##wait all proccessor to finish
    prB.join()
    prR.join()
    prG.join()

    ##End
    print("all end")