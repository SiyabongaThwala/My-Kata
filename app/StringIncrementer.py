
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]

    if head == "":
        print(strng + "1")
    else:
        print(head + str(int(tail)+1).zfill(len(tail)))   


increment_string('foobar0099')    
    


