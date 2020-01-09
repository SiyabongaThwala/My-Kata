def longest(firstString, secondString):
    combinedStrings = ''.join(sorted(set(firstString + secondString)))
    print(combinedStrings)
  
longest('siyabonga','thwala')  