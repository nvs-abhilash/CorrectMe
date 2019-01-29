import pytest

from correctme.edit_distance import EditDistance, levenshtein_distance


@pytest.mark.parametrize('str1, str2, expected_output', [
    ("dog", "dag", 1),
    ("dog", "dog", 0),
    ("abcd", "", 4),
    ("", "", 0),
    ("qwerty", "qw", 4),
    ("abcd", "efgh", 4)
])
def test_levenshtein_distance(str1, str2, expected_output):
    assert levenshtein_distance(str1, str2) == expected_output


@pytest.mark.parametrize('str1, str2', [
    ("dog", "dag"),
    ("dog", "dog"),
    ("abcd", ""),
    ("", ""),
    ("qwerty", "qw"),
    ("abcd", "efgh")
])
def test_edit_distance(str1, str2):
    ed = EditDistance(dist_func=levenshtein_distance)
    assert ed.get_edit_distance(str1, str2) == levenshtein_distance(str1, str2)
