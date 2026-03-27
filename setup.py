from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements.txt file and converts it 
    into a clean list of library names for Python to install.
    '''
    requirements = []
    
  
    with open(file_path) as file_obj:

        raw_lines = file_obj.readlines()

        for req in raw_lines:
           
            cleaned_req = req.replace("\n", "")
            if cleaned_req != HYPEN_E_DOT:
                requirements.append(cleaned_req)

    return requirements

setup(
    name='ML_project',
    version='0.0.1',
    author='harshit',
    author_email='harshitpurohit953@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)








'''def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        l1=file_obj.readlines();
        for req in l1:
            req.replace("\n","")
            requirements.append(req)
    
    return requirements'''