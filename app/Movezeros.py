
array = []

def move_zeros(array):
    if len(array) < 1:
        print (array)
    else:
        list = []
        zeros = 0

        for item in array:
            if not item and type(item) is int or type(item) is float:
                zeros += 1
            else:
                list.append(item)

        for item in range(0, zeros):
            list.append(0)
    
        print(list) 
         
       

move_zeros(array)        