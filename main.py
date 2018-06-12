# 1. Load BK Tree
# 2. Make the double_metaphone HASH
# 3. Combine the results

from correctme import bk_tree as bt
from correctme import double_metaphone as dm
from correctme import edit_distance as ed
import fuzzy

def initializeApp ():
    tree = bt.BKTree(ed.get_edit_distance, bt.dict_words('data/google-10000-english-no-swears.txt'))
    meta_dict = dm.load_metaphone_dictionary('data/google-10000-english-no-swears.txt')

    return [tree, meta_dict]

def getSuggestion (word, tree, meta_dict):
    dmeta = fuzzy.DMetaphone()

    wordsList = tree.query(word, 1)

    wordsList1 = []
    wordsList2 = []
    # for removing the edit distance value present in wordList
    for i in range (0, len(wordsList)):
        wordsList1.append( wordsList[i][1])

    dmeta_result = dmeta(word)

    if dmeta_result[0] is not None:
        key1 = dmeta_result[0]
        try:
            wordsList2 = meta_dict[key1]
        except KeyError:
            pass

        if dmeta_result[1] is not None:
            key2 = dmeta_result[1]
            try:
                wordsList2.extend (meta_dict[key2])
            except KeyError:
                pass

    # Find intersection of the two list
    wordsList3 = list (set(wordsList1) & set(wordsList2))

    return [wordsList1, wordsList2, wordsList3]

def main():
    tree, meta_dict = initializeApp()
    wordsList1, wordsList2, wordsList3 = getSuggestion ('more', tree, meta_dict)

    print (wordsList1, wordsList2, wordsList3)

if __name__ == "__main__":
    main()
