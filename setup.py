from typing import List
from setuptools import setup, find_packages

Hyphen_e_dot = '-e .'
def get_requirements(file_path)-> List[str]:
    requirements=[]
    try:
         with open(file_path) as f:
            requirements = f.readlines()
            requirements = [req.replace('\n','') for req in requirements]
            if Hyphen_e_dot in requirements:
                requirements.remove(Hyphen_e_dot)
    except FileNotFoundError:
        pass
    return requirements

setup(
    name='BearingFaultDetection',
    version='0.0.1',
    authors='Sai akshay , Sai Shreyansh , Kanishka',
    author_email='saiakshay924@gmail.com , saishreyansh2210@gmail.com , tkanishka700@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)