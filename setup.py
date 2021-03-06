#!/usr/bin/env python
from setuptools import setup, find_packages


def install():
    desc = 'A Python client library for animeultime!'
    setup(
        name='pyanimeultime',
        version='0.1',
        description=desc,
        long_description=desc,
        author='stackexploit',
        author_email='',
        url='https://github.com/stackexploit/pyanimeultime',
        classifiers=['Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3.2',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3 :: Only'
                     ],
        packages=find_packages(),
        install_requires=[
            'requests',
            'beautifulsoup4'
        ],
    )


if __name__ == "__main__":
    install()
