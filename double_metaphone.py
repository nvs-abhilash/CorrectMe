import fuzzy

def load_metaphone_dictionary():
    metaphone_dictionary = {}
    dmeta = fuzzy.DMetaphone()

    with open("google-10000-english-no-swears.txt", "r") as file:
        for word in file:
            word = word.strip()
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


# if __name__ == "__main__":
#     meta_dict = load_metaphone_dictionary()
#     print meta_dict

