import fuzzy


def load_metaphone_dictionary(path):
    metaphone_dictionary = {}
    dmeta = fuzzy.DMetaphone()

    with open(path, "r") as file:
        for word in file:
            word = word.strip()  # To strip newline characters from the end of the word.
            dmeta_result = dmeta(word)

            if dmeta_result[0] is not None:
                if dmeta_result[0] in metaphone_dictionary:
                    metaphone_dictionary[dmeta_result[0]].append(word)
                else:
                    metaphone_dictionary[dmeta_result[0]] = [word]

            if dmeta_result[1] is not None:
                if dmeta_result[1] in metaphone_dictionary:
                    metaphone_dictionary[dmeta_result[1]].append(word)
                else:
                    metaphone_dictionary[dmeta_result[1]] = [word]

        return metaphone_dictionary
