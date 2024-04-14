from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This Fucntion will return list of requirements under requirements.txt file
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return(requirements)


setup(
name='MLEndToEndProject',
version='0.0.1',
author='Ankit S',
author_email='s.ankit2087@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)
