INSERT_COST =  1
SUBSTITUTION_COST =  2
DELETE_COST =  1


def levenshtein_distance(dictionaryString, inputString, prevResult, inputStringPos):
    if inputStringPos >= len(inputString):
        return prevResult[len(dictionaryString)]
    
    newResult = []
    newResult.append(inputStringPos + 1)

    for i in range(1, len(dictionaryString) + 1):
        if dictionaryString[i - 1] == inputString[inputStringPos]:
            newResult.append(prevResult[i - 1])
        else:
            newResult.append(min(newResult[i - 1] + INSERT_COST, prevResult[i] + DELETE_COST, prevResult[i - 1] + SUBSTITUTION_COST))
        
    inputStringPos += 1
    return levenshtein_distance(dictionaryString, inputString, newResult, inputStringPos)


def get_edit_distance(dictionaryString, inputString):
    dictionaryString = lower(dictionaryString)
    inputString = lower(inputString)

    if(dictionaryString == inputString):
        edit_distance = 0
    else:
        prevResult = []
        for i in range(len(dictionaryString) + 1):
            prevResult.append(i)
        edit_distance = levenshtein_distance(dictionaryString, inputString, prevResult, 0)

    return edit_distance


#  if __name__ == "__main__":
#      print get_edit_distance("abc", "adcb")