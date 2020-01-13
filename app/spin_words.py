def spin_words(sentence:str):
    reversedString= ""
    for item in sentence.split():
        if len(item) >= 5:
            reversedWord = ''.join(reversed(item))
            reversedString =reversedString +' '+ reversedWord   
            reversedString.replace(" ","")         
        else:
            reversedString =item +' '+ reversedString
            reversedString.replace(" ","") 
             
    print(reversedString) 

spin_words('Hey fellow warriors')
