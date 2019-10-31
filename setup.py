'''
lambdata - a collection of datascience helper functions for lambdaschool
'''
import setuptools

REQUIRED = [
    "pandas",
    "numpy",
    "pytest"
]
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
    name="Nckflannery_lambdata",
    version = "0.2.40",
    author = "Nckflannery",
    description = "A collection of data science helper functions",
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://nckflannery.github.io/",
    packages=setuptools.find_packages(),
    package_data={'':['*.csv']},
    python_requires=">=3.5",
    install_requires = REQUIRED,
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ]
    )