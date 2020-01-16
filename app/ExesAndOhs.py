def xo(stringName): 
    listofchars = list(stringName)
    numberofx=listofchars.count('x')
    numberofo=listofchars.count('o')
    if (numberofx == numberofo) or (numberofo == 0 and numberofx ==0):
        print(True)
    else:
        print(False)

xo('Xoox')
    #return True
