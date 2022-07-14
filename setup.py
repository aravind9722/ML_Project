from setuptools import setup
from typing import List



# Variables for setup
PROJECT_NAME= "housing-price-predictor"
VERSION= "0.0.1"
AUTHOR= "Aravind"
DESCRIPTION="US-Housing Price predictor ML project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requiremnts.txt"

def get_requirements_list()->List(str):
    """
    Description: Function is going to return list of requirement
    mentioned in requirements.txt file

    returns: This function gives list which contains name of libraries
    mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME)as requirement_file:
        return requirement_file.readlines()


setup(
name= PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())