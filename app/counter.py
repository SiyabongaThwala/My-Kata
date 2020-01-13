# def duplicate_count(text: str):
text = "aabBcde"

def duplicate_count(text: str):
    
    dup = []
    seen = []
    
    for letter in text.lower():
        if letter in seen:
            if letter not in dup:    
                dup.append(letter)
        seen.append(letter)
      
    return(len(dup))
    

    seen = set()
    dupes = set()
    for char in text.lower():
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)

count = duplicate_count(text)
print(count)


text = "aabbcdef"
