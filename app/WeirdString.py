def to_weird_case(string):
    NewString = ""
    splittedString = (string.split())
    for item in splittedString:
        for index in range(len(item)):
            if index % 2 == 0:
                NewString += item[index].upper()
            else:    
                NewString += item[index].lower() 
        NewString = NewString + ' '            
    print(NewString.strip())        

               
           
to_weird_case("This is a test")
