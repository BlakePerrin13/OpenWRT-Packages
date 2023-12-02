from setuptools import setup, find_packages

setup(
    name='python_hello',
    version='0.1.0',
    url='https://github.com/BlakePerrin13/OpenWRT-Packages/tree/main/Packages/Python.git',
    author='Blake Perrin',
    author_email='blake.perrin13@gmail.com',
    description='Python Hello World',
    packages=find_packages(),    
    install_requires=[''],
    py_modules=[
        'hello.py',
    ],
)
