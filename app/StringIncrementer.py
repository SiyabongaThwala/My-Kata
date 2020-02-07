def increment_string(strng):
    if strng[len(strng)-1].isdigit():
        IncreasedlastValue =str(int(strng[len(strng)-1]) + 1)
        IncrementedString = strng[:-1] + IncreasedlastValue
    else:
         IncrementedString = strng + str(1)   

    print(IncrementedString)     
increment_string('foobar099')    