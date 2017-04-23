# 1. Load BK Tree
# 2. Make the double_metaphone HASH
# 3. Combine the results

import bk_tree as bt
import double_metaphone as dm
import levenshtein_distance as ld
import fuzzy

def initializeApp ():
    tree = bt.BKTree(ld.get_edit_distance, bt.dict_words('./google-10000-english-no-swears.txt'))
    meta_dict = dm.load_metaphone_dictionary('./google-10000-english-no-swears.txt')

    return [tree, meta_dict]

def getSuggestion (word):
    tree, meta_dict = initializeApp ()
    dmeta = fuzzy.DMetaphone()
    
    wordsList = tree.query(word, 1)
    
    wordsList1 = []
    for i in range (0, len(wordsList)):
        wordsList1.append( wordsList[i][1])

    dmeta_result = dmeta(word)

    if dmeta_result[0] is not None:
        key1 = dmeta_result[0]
        wordsList2 = meta_dict[key1]

        if dmeta_result[1] is not None:
            key2 = dmeta_result[1]
            wordsList2.append (meta_dict[key2])

    # Find intersection of the two list
    wordsList3 = list (set(wordsList1) & set(wordsList2))
    
    return [wordsList1, wordsList2, wordsList3]

def main():
    wordsList1, wordsList2, wordsList3 = getSuggestion ('more')
    
    print (wordsList1, wordsList2, wordsList3)

if __name__ == "__main__":
    main()