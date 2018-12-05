# CorrectMe
#### A context based auto-correction python package

CorrectMe is a context based auto-correction python package, also available with a GUI for demo purposes. It recommends correct words for misspellings by learning from the context.

Currently the project is in very early stages, and no stable behavior can be expected.

All contributions are welcomed :)

## Installation

Please use `Python3.x` for working with the package.

Creating a virtual environment is recommended as the code is in pre-release. Below steps are shown for conda environment.

```bash
conda create -n cm_env python=3.6 pip
source activate cm_env # activate cm_env for windows
cd CorrectMe # The cloned repository directory
pip install .
```

To test your installation, move the `main.py` file from the repository to another location, and run it.

```bash
python main.py
```
Note: moving is required as otherwise, `correctme` will be imported from the repository itself.

## Current status of the project

The project is in very early stages, and the packages don't have clear naming conventions, or lack documentation. This project was part of authors' Information Retrieval project. Work needs to be done to make it a useful python package.

Contributions to this project in the form of opening relevant issues, submitting PRs for new code or documentation is highly welcomed.  

Continuous development on this project cannot be guarenteed at the moment as the authors contribute to the project in their free time out of interest.

## Algorithms used in the project

The idea is to make a context based correction package, where the package would perform auto-corrections, provide suggestions for corrections as well.

* Currently we have used bk_tree for finding closest words using Minimum Edit Distance.
* Double metaphones to get closest words according to phonetics.

Lots of future work has to be done with adding new and efficient algorithms to it.

## GUI of the code

Currently we are using `Kivy` for the GUI so as to support multiple platforms.   

The GUI is very naive and not at all well documented. Lots of redundant codes are also present. Would like to change it ASAP. Adding issues for those also makes our work faster.

## Documentation

Currently lots of things are not documented well. Documentations explaining how to use the code base, simple tutorials explaining concepts are also useful and are definitly on the TODO lists of the authors. Any help is highly appreciated. Opening an issue for the same or submitting PRs are useful. I know said it many times now ;)
