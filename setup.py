"""
Setup.py file is for distribution of package , i.e for versioning of the project

https://docs.python.org/3/distutils/setupscript.html #Setup.py script available

Version should be changed before publish

"""

from setuptools import find_packages, setup
from typing import List

requriment_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."

#setup file is required to treat the project as python library so that we can use it as a library in
# another projec
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements() -> List[
    str]:  # arrow function is just an annotation just to provide information that it will return list of strings
    with open(REQUIREMENT_FILE_NAME) as requirement_file:  # there is a \n in requirements.txt it is not visible
        requirement_list = requirement_file.readlines()
        requirement_list = [i.replace('\n', "") for i in requirement_list]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    print(requirement_list)
    return requirement_list


setup(name='ExpensePrediction',
      version='0.0.1',
      description='Predicting Expenses based on Lifestyle for Insurance',
      author='PritamPatra',
      author_email='pritampatra988@gmail.com',
      packages=find_packages(),  # finds folder with __init__.py file in Insurance Package
      install_requires=get_requirements()  # searches for requirement.txt file to install libraries
      )
