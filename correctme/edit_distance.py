def levenshtein_distance(dictionaryString, inputString):

    def levenshtein_distance_helper(dictionaryString, inputString, prevResult, inputStringPos):
        if inputStringPos >= len(inputString):
            return prevResult[len(dictionaryString)]

        newResult = []
        newResult.append(inputStringPos + 1)

        for i in range(1, len(dictionaryString) + 1):
            if dictionaryString[i - 1] == inputString[inputStringPos]:
                newResult.append(prevResult[i - 1])
            else:
                newResult.append(
                    min(newResult[i - 1] + insert_cost, prevResult[i] + delete_cost,
                        prevResult[i - 1] + substitution_cost))

        inputStringPos += 1
        return levenshtein_distance_helper(dictionaryString, inputString, newResult, inputStringPos)

    insert_cost = 1
    substitution_cost = 2
    delete_cost = 1
    prevResult = [i for i in range(len(dictionaryString) + 1)]
    return levenshtein_distance_helper(dictionaryString, inputString, prevResult, inputStringPos=0)


# Call this function when making API calls.
class EditDistance:
    def __init__(self, dist_func=levenshtein_distance):
        self._dist_func = dist_func

    def get_edit_distance(self, dictionary_string, input_string):
        dictionary_string = dictionary_string.lower()
        input_string = input_string.lower()

        if dictionary_string == input_string:
            edit_distance = 0
        else:
            edit_distance = self._dist_func(dictionary_string, input_string)

        return edit_distance
