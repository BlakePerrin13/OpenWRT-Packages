from setuptools import setup, find_packages

setup(
    name='python3-helloworld',
    version='1.0',
    url='https://github.com/BlakePerrin13/OpenWRT-Packages/tree/main/Packages/Python',
    author='Blake Perrin',
    author_email='blake.perrin13@gmail.com',
    description='OpenWRT Python Hello World Program',
    packages=find_packages(),    
    install_requires=[''],
    py_modules=[
        'python3-helloworld.py',
    ],
)
