""" BK Tree implementation """


class BKTree:
    """ Class of BK Tree """

    def __init__(self, distfn, words):
        """
        Create a new BK-tree from the given distance function and
        words.
        Arguments:
        distfn: a binary function that returns the distance between
        two words.  Return value is a non-negative integer.  the
        distance function must be a metric space.
        words: an iterable.  produces values that can be passed to
        distfn
        """
        self.distfn = distfn

        it = iter(words)
        root = next(it)
        self.tree = (root, {})

        for i in it:
            self._add_word(self.tree, i)

    def _add_word(self, parent, word):
        pword, children = parent
        d = self.distfn(word, pword)
        if d in children:
            self._add_word(children[d], word)
        else:
            children[d] = (word, {})

    def query(self, word, n):
        """
        Return all words in the tree that are within a distance of `n'
        from `word`.
        Arguments:

        word: a word to query on
        n: a non-negative integer that specifies the allowed distance
        from the query word.

        Return value is a list of tuples (distance, word), sorted in
        ascending order of distance.

        """

        def rec(parent):
            pword, children = parent
            d = self.distfn(word, pword)
            results = []
            if d <= n:
                results.append((d, pword))

            for i in range(d - n, d + n + 1):
                child = children.get(i)
                if child is not None:
                    results.extend(rec(child))
            return results

        # sort by distance
        return sorted(rec(self.tree))


def brute_query(word, words, distfn, n):
    """A brute force distance query
    Arguments:
    word: the word to query for
    words: a iterable that produces words to test
    distfn: a binary function that returns the distance between a
    `word' and an item in `words'.
    n: an integer that specifies the distance of a matching word

    """
    return [i for i in words
            if distfn(i, word) <= n]


def max_depth(tree, count=0):
    _, children = tree
    if len(children):
        return max(max_depth(i, count + 1) for i in list(children.values()))
    else:
        return count


def dict_words(dictfile):
    "Return an iterator that produces words in the given dictionary."
    return filter(len, map(str.strip, open(dictfile)))
