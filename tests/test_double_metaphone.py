from correctme.double_metaphone import DoubleMetaphone


def test_double_metaphone():
    dataset_file = r'correctme/data/google-10000-english-no-swears.txt'
    dm = DoubleMetaphone(dataset_file)
    dm.load_metaphone_dictionary()
    assert len(dm.metaphone_dictionary) != 0
