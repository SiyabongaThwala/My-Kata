PossibleCombinations = [':)',':D',':~)',':~D',':-D',':-)',';-D',';~D',';)',';-)',';D',';~)']
InputArray = []
def count_smileys(InputArray):
    numberOfSmileyFace = 0
    for item in InputArray:
        if item in PossibleCombinations:
            numberOfSmileyFace += 1
    print(numberOfSmileyFace)

count_smileys(InputArray)

    #return #the number of valid smiley faces in array/list