# http://en.wikibooks.org/wiki/Algorithm_implementation/Strings/Levenshtein_distance#Python
def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    d = [list(range(n + 1))]
    d += [[i] for i in range(1, m + 1)]
    for i in range(0, m):
        for j in range(0, n):
            cost = 1
            if s[i] == t[j]: cost = 0

            d[i + 1].append(min(d[i][j + 1] + 1,  # deletion
                                d[i + 1][j] + 1,  # insertion
                                d[i][j] + cost)  # substitution
                            )
    return d[m][n]


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
