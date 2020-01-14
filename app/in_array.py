a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
def in_array(a1,a2): 
    l=[] 
    for word in a2: 
        for item in a1: 
            if item in word: 
                l.append(item)
    if l(item) > 1             
        print((list(set(l))))
    else:
        print("")    

'''
def spin_words(sentence:str):
    splittedString = list(sentence)
    splittedString.reverse()
    reversedString = ''.join(splittedString)
    
    return reversedString

    reversedString= ""
    for item in sentence.split():
        if len(item) >= 5:
            reversedWord = ''.join(reversed(item))
            reversedString =reversedString +' '+ reversedWord           
        else:
            reversedString =item +' '+ reversedString
    if len(sentence.split()) == 1:
        finalString=reversedString.strip()
        print(finalString) 
    else:
        reversedString
        print(reversedString)

'''    