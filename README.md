# CorrectMe
#### A context based auto-correction python package

CorrectMe is a context based auto-correction python package, also available with a GUI for demo purposes. It learns from the context what could be the correct words to recommend.

Currently the project is in very early stages, and no stable behavior can be expected.

All contributions are welcomed :)

## Installation

Please use `Python3.x` for working with the package.

### 1. Kivy installation

Installation of Kivy is buggy, only working way for the author is given bellow. Please share other methods if found working with the project.

Installation using sources seems to work fine with version `kivy==1.10.1`

Please follow the following link: [Development Version](https://kivy.org/docs/installation/installation.html#installation-devel)

### 2. Fuzzy installation

`pip install fuzzy`

### 3. CorrectMe installation

Currently no installation option is provided. To use the package `cd` into the root directory and import the packages.

## Current status of the project

The project is in very early stages, and the packages don't have clear naming conventions, or lacks documentations. This project was part of authors' Information Retrieval project. Work needs to be done to make it an useful python package.

Contributions to this project in the form of opening relevant issues, submitting PRs for new code or documentation is highly welcomed.  

Continuous development on this project cannot be guarenteed at the moment as the authors contribute to the project in their free time out of interest.

## Algorithms used in the project

The idea is to make a content based correction package, where the package would do auto-corrections, give suggestions for corrections as well.

* Currently we have used bk_tree for finding closest words using Minimum Edit Distance.
* Double metaphones to get closest words according to phonetics.

Lots of future work has to be done with adding new and efficient algorithms to it.

## GUI of the code

Currently we are using `Kivy` for the GUI so as to support multiple platforms.   

The GUI is very naive and not at all well documented. Lots of redundant codes are also present. Would like to change it ASAP. Adding issues for those also makes our work faster.

## Documentation

Currently lots of things are not documented well. Documentations explaining how to use the code base, simple tutorials explaing concepts are also useful and are definitly on the TODO lists of the authors. Any help is highly appreciated. Opening an issue for the same or submitting PRs are useful. I know said it many times now ;)
