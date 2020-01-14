listOfNumbers = [20, 37, 21]
duplicatesAllowed = 2

def delete_nth(listOfNumbers,duplicatesAllowed):
    newlist =[]
    for item in listOfNumbers:
        if newlist.count(item) < duplicatesAllowed:
            newlist.append(item)    
    print(newlist)         

delete_nth(listOfNumbers,duplicatesAllowed)