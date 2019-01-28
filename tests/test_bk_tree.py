from functools import partial

import pytest

from correctme.bk_tree import BKTree
from correctme.edit_distance import EditDistance, levenshtein_distance


@pytest.fixture
def build_bktree():
    words = ['a', 'ab', 'abc', 'abcd']
    ed = EditDistance(dist_func=levenshtein_distance)
    distfn = partial(ed.get_edit_distance)
    bktree = BKTree(distfn, words)
    return bktree


@pytest.mark.parametrize('test_word, test_dist, test_out', [
    ('a', 0, [(0, 'a')]),
    ('a', 2, [(0, 'a'), (1, 'ab'), (2, 'abc')]),
    ('ab', 2, [(0, 'ab'), (1, 'abc'), (1, 'a'), (2, 'abcd')]),
    ('abcd', 1, [(0, 'abcd'), (1, 'abc')]),
    ('a', 10, [(0, 'a'), (1, 'ab'), (2, 'abc'), (3, 'abcd')])
])
def test_bktree(build_bktree, test_word, test_dist, test_out):
    tree = build_bktree
    assert set(tree.query(test_word, test_dist)) == set(test_out)
