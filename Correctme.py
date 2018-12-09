from os import path

from correctme.ui.gui import CorrectMeApp
import correctme.data

DATASET_FILE = r'google-10000-english-no-swears.txt'


def run():
    data_dir = path.dirname(correctme.data.__file__)
    dataset = path.join(data_dir, DATASET_FILE)
    CorrectMeApp(dataset).run()

if __name__ == "__main__":
    run()
