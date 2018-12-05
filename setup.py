"""Setup module for CorrectMe"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='correctme',  # Required

    version='0.0.1',  # Required

    description='A context based autocorrection application',  # Optional

    long_description=long_description,  # Optional

    long_description_content_type='text/markdown',  # Optional (see note above)

    url='https://github.com/nvs-abhilash/CorrectMe',  # Optional

    author='Piyush Jaiswal and NVS Abhilash',  # Optional
    
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='nlp',  # Optional

    python_requires='>=3',
    packages=find_packages(exclude=['contrib', 'docs', 'tests',\
                                    'user_dictionaries']),  # Required

    install_requires=['fuzzy', 'kivy==1.10.1'],  # Optional

    include_package_data=True
    # May need in the future
    # extras_require={  # Optional
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # TODO: Make use of this to provide a default script 
    #data_files=[('google_10K-en.txt', ['data/google-10000-english-no-swears.txt'])],  # Optional

    # May need in future
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    # May need in future to refere the papers
    # project_urls={  # Optional
    #     'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #     'Funding': 'https://donate.pypi.org',
    #     'Say Thanks!': 'http://saythanks.io/to/example',
    #     'Source': 'https://github.com/pypa/sampleproject/',
    # },
)
