#!/usr/bin/env python3
'Define the interview-python-api Python package'

import setuptools

setuptools.setup(
    name='interview_python_api',
    version='0.0.1',
    author='Tom McKeesick',
    author_email='tom.mckeesick@lexer.com.au',
    description='The lexer internal fake Python API for job applicants',
    long_description='The lexer internal fake Python API for job applicants',
    long_description_content_type='text/markdown',
    url='https://github.com/lexerdev/interview-python-api',
    packages=setuptools.find_packages(),
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [],
    },
    install_requires=[]
)
