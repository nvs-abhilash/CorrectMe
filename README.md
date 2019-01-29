# CorrectMe
#### A context based auto-correction python package

CorrectMe is a context based auto-correction python package, also available with a GUI for demo purposes. It recommends correct words for misspellings by learning from the context.

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

### Working with the package

```python
import correctme
```
Then you can call any of the `correctme` functions. 

**NOTE**: API docs are not present yet. Contributing to docs are welcome. (Issue [#27](https://github.com/nvs-abhilash/CorrectMe/issues/27))

### Working with the GUI

Type the below command in the terminal:
```bash
correctme-gui
```
This will pop up the GUI for the project, and you would also see the predictions in the terminal.

## Current status of the project

### Completed
* Performs distance based and phoneme based corrections.
* Installable Python library.
* Workable Kivy GUI.
* Almost complete test suite in pytest

### WIP
* Still doesn't perform context based correction (Issue [#20](https://github.com/nvs-abhilash/CorrectMe/issues/20))
* Lacks documentation API docs, and user documentation. (Issue [#27](https://github.com/nvs-abhilash/CorrectMe/issues/27))

## Algorithms used in the project

The idea is to make a context based correction package, where the package would perform auto-corrections, provide suggestions for corrections as well.

* Currently used algorithms:
  - `bk_tree` for finding closest words using Minimum Edit Distance.
  - `double_metaphone` to get closest words according to phonetics.
