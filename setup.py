from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''
    This funbction will return the list of requirements
    '''
    reqiurements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove('-e .')

    return requirements

setup(
name = 'MLProject',
version='0.0.1',
author= 'Vraj',
author_email='vrajcbhavsar0905@gmail.com',
packages=find_packages(),
insatll_requires= get_requirements('requirements.txt')
)