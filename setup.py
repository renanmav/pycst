#!/usr/bin/env python
from os.path import join

from setuptools import setup, find_packages

MODULE_NAME = 'pycst'           # package name used to install via pip (as shown in `pip freeze` or `conda list`)
MODULE_NAME_IMPORT = 'pycst'    # this is how this module is imported in Python (name of the folder inside `src`)
REPO_NAME = 'pycst'             # repository name


def requirements_from_pip(filename='requirements.txt'):
    with open(filename, 'r') as pip:
        return [l.strip() for l in pip if not l.startswith('#') and l.strip()]


def get_long_description(filename='README.md'):
    with open(filename, 'r') as file:
        return file.read()

setup(
    name=MODULE_NAME,
    description="CST Studio Suite API for python",
    url='https://github.com/renanmav/{:s}'.format(REPO_NAME),
    author='Renan Machado',
    author_email='renan.mav@hotmail.com',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    version=(open(join('src', MODULE_NAME, 'resources', 'VERSION')).read().strip()),
    install_requires=requirements_from_pip(),
    extras_require={"test_deps": requirements_from_pip('requirements_test.txt')},
    include_package_data=True,
    zip_safe=False,
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: Microsoft :: Windows'],
    long_description=get_long_description(),
    long_description_content_type='text/markdown'
)
