import setuptools
from setuptools.command.install import install
import nltk
import subprocess
import sys
    

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='0.1.0',
    description='Python project',
    author='Nikita and Tech titans',
    author_email='k.nikita4487@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=[
        'asgiref==3.8.1',
        'click==8.1.7',
        'Django>=4.1.9',
        'joblib==1.4.2',
        'regex==2024.9.11',
        'sqlparse>=0.4.4',
        'tqdm==4.66.5',
        'setuptools==74.1.2',
        'nltk',
    ],
    setup_requires=['nltk', 'joblib', 'click', 'regex', 'sqlparse', 'setuptools'],
   
)
