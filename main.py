from os.path import join

from correctme.ui.gui import SimpleKivy

DATASET_FILE = r'google-10000-english-no-swears.txt'


def main():
    dataset = join(r'data', DATASET_FILE)
    SimpleKivy(dataset).run()


if __name__ == "__main__":
    main()
