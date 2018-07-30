from os.path import join

from correctme.ui.gui import CorrectMeApp

DATASET_FILE = r'google-10000-english-no-swears.txt'


def main():
    dataset = join(r'data', DATASET_FILE)
    CorrectMeApp(dataset).run()

if __name__ == "__main__":
    main()
