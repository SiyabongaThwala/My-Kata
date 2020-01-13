'''
def longest(firstString, secondString):
    combinedStrings = ''.join(sorted(set(firstString + secondString)))
    print(combinedStrings)
  
longest('siyabonga','thwala')  
'''
count = {}
def duplicate_count(text):
    for item in text:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    for key in count:
        if count[key] > 1:
            print(key,count[key])



        

