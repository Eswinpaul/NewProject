from setuptools import find_packages, setuptools
from distutils.core import setup
from typing import List

def get_requirements(filepath:str)-> List[str]:
    HYP = "-e ."
    requirements = []
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
        if HYP in requirements:
            requirements.remove(HYP)
    return requirements            


setup(
    name = 'Classification Project',
    version = '1.0.0',
    author = 'Eswin Paul',
    author_email = 'eswinpaul1994@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    )