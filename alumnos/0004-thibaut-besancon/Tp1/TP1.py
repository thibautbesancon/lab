# coding:utf-8
import multiprocessing
import time

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
    ##Take a filename ppm and cut the header and the body
    header, body = takeppm("image.ppm")

    ##Creation of  the 3 process in different processor
    prB = multiprocessing.Process(target=process_blue(header, body))
    prR = multiprocessing.Process(target=process_red(header, body))
    prG = multiprocessing.Process(target=process_green(header, body))

    ##Start the process 
    print("bluestart")
    prB.start()
    print("redstart")
    prR.start()
    print("greenstart")
    prG.start()

    ##wait all proccessor to finish
    prB.join()
    prR.join()
    prG.join()

    ##End
    print("all end")