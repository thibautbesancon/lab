import time
import array
import sys
import argparse
import threading

cad = threading.Lock()
pixels_list = []


def Message_to_Binary(message):
    messagebin = ''.join(format(ord(i), "08b") for i in message)
    return messagebin

def Binary_to_Octal(binary):
    i = 0
    for value in binary:
        if i != 0:
            tmplist = tmplist + str(value)
        else:
            tmplist = str(value)
        i += 1
    i=0 ; j=0 ; bintmp = 0 ; binarylist = []
    for value in tmplist:
        if(j!=4):
            bintmp = bintmp*10 + int(value)
        else:
            bintmp = bintmp+10000
            tmp = str(bintmp)
            tmp = tmp[1]+tmp[2]+tmp[3]+tmp[4]
            binarylist.append(tmp)
            bintmp = int(value)
            j = 0
        i += 1 ; j += 1

    bintmp = bintmp + 10000
    tmp = str(bintmp)
    tmp = tmp[1] + tmp[2] + tmp[3] + tmp[4]
    binarylist.append(tmp)

    return binarylist

def Integer_to_Octal(integerlist):
    messagebin = []
    for i in integerlist:
        tmp = f'{i:08b}'
        messagebin.append(tmp)
    return Binary_to_Octal(messagebin)

def Octal_to_IntegerList(octallist):
    messageint = []

    for i in range(1,len(octallist), 2):
        tmp = octallist[i-1]+octallist[i]
        messageint.append(int(tmp, 2))
    return messageint



def Eliminate_return_line(document):
    for i in range(document.count(b"\n#")):
        first_commentary = document.find(b"\n#")
        last_commentary = document.find(b"\n#", first_commentary + 1)
        document = document.replace(document[first_commentary:last_commentary], b"")
    return (document)


def Get_pixels_list(document):
    global pixels_list
    header = document[:15].decode()  # decode the first 15 character of the document
    header = header.replace("P6", "P3")  # get the magic number P3
    return (header)


def process(bodypixel,color, message):
    i=0
    bodyoct = Integer_to_Octal(bodypixel)

    msglen = len(message)
    for x in range(color*2+1,len(bodyoct), 6):
        if i < msglen:
            bodyoct[x] = message[i]
        i+=3
    bodyint = Octal_to_IntegerList(bodyoct)
    return bodyint

def processPixel(color, message):
    body = process(pixels_list,color, message)
    for x in range(color,len(body), 3):
        pixels_list[x] = body[x]
    #return bodypixel




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Staganography program")
    parser.add_argument("-p", "--offset", default="0", help="First pixel to be change")
    parser.add_argument("-i", "--interleave", default="1", help="Frequence of pixels change")
    parser.add_argument("-s", "--size", default="3", help="Reading bloc")
    parser.add_argument("-f", "--file", default="dog.ppm", help="Image file")
    parser.add_argument("-m", "--message", default="message.txt", help="Message file")
    parser.add_argument("-o", "--output", default="stegano.ppm", help="Output file")
    args = parser.parse_args()

    if int(args.offset) < 0:
        print("This value can't be negative")
        sys.exit()
    elif int(args.interleave) <= 0:
        print("This value must be positive")
        sys.exit()
    elif int(args.size) <= 0 or int(args.size) % 3 != 0:
        print("Error with the size : it must be positive and a multiple of 3")

    try:
        image_doc = open(args.file, "rb")
    except FileNotFoundError:
        print("The document is not in the folder")
        sys.exit()

    mes = open(args.message, "r")  # open the message file and put it in a list
    letters = mes.read()
    mes.close()
    message_list = []
    for x in letters:
        binary = Message_to_Binary(x)
        message_list.append(binary)                                                                             #message size
    octal_list = Binary_to_Octal(message_list)

    image_doc = open(args.file, "rb")
    image = image_doc.read(1024)
    header = Get_pixels_list(Eliminate_return_line(image))

    # print(header)
    first_commentary = image.find(b"\n#")  # see where are the pixels in the image
    last_commentary = image.find(b"\n#", first_commentary + 1)
    beginning_body = len(header) + (last_commentary - first_commentary)
    image_doc.seek(beginning_body)  # go to the offset position
    reading = image_doc.read()
    pixels_list = [x for x in reading]  # put the elements in the list

    bodypixel = pixels_list

    indice_red = 0
    indice_green = 1
    indice_blue = 2


    red_thread = threading.Thread(target=processPixel, args=(indice_red, octal_list))  # set up the threads
    green_thread = threading.Thread(target=processPixel, args=(indice_green, octal_list))
    blue_thread = threading.Thread(target=processPixel, args=(indice_blue, octal_list))

    time.sleep(1)  # start and join the threads
    red_thread.start()
    time.sleep(1)
    green_thread.start()
    time.sleep(1)
    blue_thread.start()

    red_thread.join()
    green_thread.join()
    blue_thread.join()

    final_doc = open(args.output, "w")  # open the document to write the header in it
    final_doc.write(header + "\n")
    final_doc.close()
    final_doc = open(args.output, "a")  # open the document to append
    final_doc.write("#UMCOMPU2 " + args.offset + " " + args.interleave + " " + str(len(message_list)) + "\n")
    final_doc.write(" ".join([str(x) for x in pixels_list]))
    final_doc.close()