def spin_words(sentence:str):
    print(" ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")]))
'''    
    reversedString= ""

    for item in sentence.split():
        if len(item) >= 5:
            a = item[len(item)::-1]
            reversedString += a + ' '
        else:
            reversedString = reversedString +' '+ item + ' '
           
    #reversedString.replace("  "," ")
    print((reversedString.strip()).replace("  "," "))
'''
spin_words('Hey fellow warriors')
