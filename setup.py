from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns the list of requirements 
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip() # For any empty spaces 
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirement.txt is not found")

    return requirement_list


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Vansh_Sachdeva",
    author_email="bh2ggsipu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)