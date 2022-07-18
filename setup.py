from setuptools import setup, find_packages
from typing import List



# Variables for setup
PROJECT_NAME= "housing-price-predictor"
VERSION= "0.0.1"
AUTHOR= "Aravind"
DESCRIPTION="US-Housing Price predictor ML project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: Function is going to return list of requirement
    mentioned in requirements.txt file

    returns: This function gives list which contains name of libraries
    mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME)as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name= PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)
