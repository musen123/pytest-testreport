#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-testreport',
    version='1.0.0',
    author='MuSen',
    author_email='musen_nmb@qq.com',
    maintainer='testreport',
    maintainer_email='musen_nmb@qq.com',
    license='MIT',
    url='https://github.com/musen123/pytest-testreport',
    description='pytest test report',
    long_description=read('README.rst'),

    py_modules=['pytest_testreport'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0'],
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
        "": ["*.html",'*.rst'],
    },
    entry_points={
        'pytest11': [
            'testreport = pytest_testreport',
        ],
    },
)
