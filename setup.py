from setuptools import find_packages, setup
from typing import List

# This constant represents the "trigger" that connects setup.py to requirements.txt
HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements.txt file and converts it 
    into a clean list of library names for Python to install.
    '''
    requirements = []
    
  
    with open(file_path) as file_obj:
        # 2. Read all lines into a temporary list
        raw_lines = file_obj.readlines()

        # 3. Clean each line using a simple FOR loop
        for req in raw_lines:
           
            cleaned_req = req.replace("\n", "")
            if cleaned_req != HYPEN_E_DOT:
                requirements.append(cleaned_req)

    return requirements

# The actual configuration of your project
setup(
    name='ML_project',
    version='0.0.1',
    author='harshit',
    author_email='your_email@example.com', # Added a placeholder for clarity
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
