from setuptools import setup, find_packages
from typing import List

Hypen_E_Dot = '-e .'
def get_requirements(file_path: str) -> List[str]:  # Use List[str] for compatibility
    """
    This function returns a list of requirements from the given file path.
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='Abhishek Shenoy',   
    author_email='abhishekshenoy84@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Keep only this
)