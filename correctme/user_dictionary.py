import pickle
import os


class personalizedDictionary:
    """
    Class containing the personal dictionary for the users. This dictionary contains every word the user has ever used
    and their frequencies!
    """
    totalRegisteredUsers = 0

    def __init__(self, userName):
        self.__name = userName
        self.loadDictionary()
        personalizedDictionary.totalRegisteredUsers += 1

    def getDictionary(self):
        return self.__dictionary

    def getName(self):
        return self.__name

    def addToDictionary(self, word):
        if word in self.__dictionary:
            self.__dictionary[word] += 1
        else:
            self.__dictionary[word] = 1

    def saveDictionary(self):
        dir_path = os.path.join("user_dictionaries")
        with open(os.path.join(dir_path, self.__name + ".dat"), "wb") as file:
            pickle.dump(self.__dictionary, file)

    def loadDictionary(self):
        dir_path = os.path.join("user_dictionaries")
        try:
            with open(os.path.join(dir_path, self.__name + ".dat"), "rb") as file:
                self.__dictionary = pickle.load(file)
        except IOError:
            self.__dictionary = {}
