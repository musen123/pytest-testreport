#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup,find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return open(file_path, encoding='utf-8').read()


setup(
    name='pytest-testreport',
    version='1.0.1',
    author='MuSen',
    author_email='musen_nmb@qq.com',
    maintainer='testreport',
    maintainer_email='musen_nmb@qq.com',
    license='MIT',
    url='https://github.com/musen123/pytest-testreport',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    # py_modules=['pytestTestreport'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    package_data={
        "": ["*.html",'*.md'],
    },
    entry_points={
        'pytest11': [
            'testreport = pytestTestreport.pytestTestreport',
        ],
    },
)
