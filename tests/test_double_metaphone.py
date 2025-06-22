from importlib import reload
import sys
import types

import correctme.double_metaphone as dm


def test_double_metaphone():
    dataset_file = r'correctme/data/google-10000-english-no-swears.txt'
    meta = dm.DoubleMetaphone(dataset_file)
    meta.load_metaphone_dictionary()
    assert len(meta.metaphone_dictionary) != 0


def test_double_metaphone_with_fuzzy(monkeypatch):
    """Ensure the real fuzzy implementation is used when available."""

    class DummyMeta:
        def __init__(self):
            self.calls = []

        def __call__(self, word):
            self.calls.append(word)
            return (word, None)

    dummy_instance = DummyMeta()

    def dummy_factory():
        return dummy_instance

    fuzzy_stub = types.SimpleNamespace(DMetaphone=dummy_factory)
    monkeypatch.setitem(sys.modules, "fuzzy", fuzzy_stub)

    reload(dm)

    dataset_file = r"correctme/data/google-10000-english-no-swears.txt"
    meta = dm.DoubleMetaphone(dataset_file)
    meta.load_metaphone_dictionary()

    assert dummy_instance.calls

    monkeypatch.delitem(sys.modules, "fuzzy", raising=False)
    reload(dm)
