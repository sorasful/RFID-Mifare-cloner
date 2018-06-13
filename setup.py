#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='rfid_mifare_cloner',
    packages=find_packages(),
    version="1.0.0",
    description='A CLI tool to clone mifare classic cards.',
    license='Unlicense',
    url='https://github.com/sorasful/RFID-Mifare-cloner',
    author='sorasful',
    entry_points={
        'console_scripts': [
            'rfid-mifare-cloner = RFID_mifare_cloner.cli:command_line',
        ]
    },
)
