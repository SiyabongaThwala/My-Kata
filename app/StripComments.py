def solution(string,markers): 
    array = string.split('\n')
    # position = string.index('#')
    # BeforMarkerString = string[:position]
    #print(array)    
    for marker in markers:
        for item in array:
            # def contains(item,marker):

            #     if
            if marker in item:
                position = item.index(marker)
                BeforeMarkerString = item[:position].strip()
                #markerIndex += 1
                print(BeforeMarkerString)
              

            

            
solution("apples, pears # and bananas\ngrapes\nbananas !apples",["#","!"]) 
# contains(sentence, marker)
    