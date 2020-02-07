def splitStrings(string):
    EvenString = ''

    if len(string) % 2 != 0:
        EvenString =''.join((string,"_"))
    else:
        EvenString = string    
   
    splitPoint = 2
    SplittedList = [(EvenString[item:item+splitPoint]) for item in range(0,len(EvenString),splitPoint)]
    print(SplittedList)


splitStrings("siyab")    