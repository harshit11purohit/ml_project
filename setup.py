from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    ''' this fxn will return list of requirements.txt '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "") for req in requirements]

    return requirements


setup(
    name='ML_project',
    version='0.0.1',
    author='harshit',
    author_email='',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)