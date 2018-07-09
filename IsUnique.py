#all unique characters

def isStringUnique(inputString):
    uniqueCharactersOnly = True;
    for letter in inputString:
        if letter in foundCharacters:
            return("the inputstring does not contain only unique characters")
        else:
            foundCharacters.add(letter)

    if uniqueCharactersOnly:
        return("the string contains only unique characters")

#all unique characters - no extra data structures
def isStringUniqueNoDataStructure(inputString):
    sortedInputString = sorted(inputString)
    previousLetter = ''
    for letter in sortedInputString:
        if previousLetter == letter:
            return ("the inputstring does not contain only unique characters")
        previousLetter = letter
    return("the string contains only unique characters")


inputString = input("Enter a string: ")
foundCharacters = set()
outString = isStringUnique(inputString)
outString2 = isStringUniqueNoDataStructure(inputString)
if outString != outString2:
    print("mep mep something went wrong")
else:
    print(outString2)




