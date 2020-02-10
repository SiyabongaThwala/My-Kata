
def increment_string(strng):
    if strng[len(strng)-1].isdigit():
        NumbersFromString=([int(item) for item in strng if item.isdigit()])
        numbertoincrease= (''.join(map(str,NumbersFromString))) #joining the numbers from the string

        IncreasedlastValue =str(int((''.join(map(str,NumbersFromString)))) + 1)
        
        IncrementedString = strng[:-1] + IncreasedlastValue
    else:
         IncrementedString = strng + str(1)   
        
    print(IncrementedString) 

    # NumbersFromString=([int(item) for item in strng if item.isdigit()])
    # print(NumbersFromString)
    # print(''.join(map(str,NumbersFromString)))
    


increment_string('foobar99')    
    