from collections import defaultdict

import fuzzy


class doubleMetaphone:
    _dmeta = fuzzy.DMetaphone()

    def __init__(self, dataset_file):
        self.metaphone_dictionary = defaultdict(list)
        self._dataset_file = dataset_file

    def load_metaphone_dictionary(self):
        with open(self._dataset_file, "r") as dataset:
            for word in dataset:
                word = word.strip()  # To strip newline characters from the end of the word.
                dmeta_result = self._dmeta(word)

                if dmeta_result[0]:
                    self.metaphone_dictionary[dmeta_result[0]].append(word)

                if dmeta_result[1]:
                    self.metaphone_dictionary[dmeta_result[1]].append(word)
