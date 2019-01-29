"""
1. Load BK Tree
2. Make the double_metaphone HASH
3. Combine the results
"""

from functools import partial

import fuzzy

from correctme import bk_tree as bt
from correctme import double_metaphone as dm
from correctme import edit_distance as ed


def initialize_app(dataset):
    ed_ob = ed.EditDistance()
    dist_func = partial(ed_ob.get_edit_distance)
    tree = bt.BKTree(dist_func, bt.dict_words(dataset))
    double_metaphone = dm.DoubleMetaphone(dataset)
    double_metaphone.load_metaphone_dictionary()

    return [tree, double_metaphone.metaphone_dictionary]


def get_suggestion(word, tree, meta_dict):
    dmeta = fuzzy.DMetaphone()

    words_list = tree.query(word, 1)

    words_list1 = []
    words_list2 = []
    # for removing the edit distance value present in wordList
    for i in range(0, len(words_list)):
        words_list1.append(words_list[i][1])

    dmeta_result = dmeta(word)

    if dmeta_result[0] is not None:
        key1 = dmeta_result[0]
        try:
            words_list2 = meta_dict[key1]
        except KeyError:
            pass

        if dmeta_result[1] is not None:
            key2 = dmeta_result[1]
            try:
                words_list2.extend(meta_dict[key2])
            except KeyError:
                pass

    # Find intersection of the two list
    words_list3 = list(set(words_list1) & set(words_list2))

    return [words_list1, words_list2, words_list3]
