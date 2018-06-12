#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    "blinker",
    "jaraco.classes>=1.1",
    "pika",
    "PikaChewie>=1.3",
    "six",
]

setup(
    name='yg.emanate',
    version='0.4.0',
    description="Lightweight event system for Python",
    author="YouGov, plc",
    author_email='dev@yougov.com',
    url='https://github.com/yougov/yg.emanate',
    packages=[
        'yg.emanate',
    ],
    namespace_packages=['yg'],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='emanate',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
)
