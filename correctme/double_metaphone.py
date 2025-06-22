from collections import defaultdict

try:  # pragma: no cover - optional dependency
    import fuzzy
    _DMetaphone = fuzzy.DMetaphone  # type: ignore
except ImportError:  # pragma: no cover - fallback when fuzzy isn't installed
    class _DMetaphone:
        """Minimal fallback implementation for DMetaphone."""

        def __call__(self, word):
            # Very small approximation: use the word itself as the key
            primary = word.lower()
            return (primary, None)


class DoubleMetaphone:
    """Wrapper around the double metaphone implementation."""

    _dmeta = _DMetaphone()

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
