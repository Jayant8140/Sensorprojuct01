from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOTE= '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if HYPEN_E_DOTE in requirements:
        requirements.remove(HYPEN_E_DOTE)
    return requirements
    

setup (
  name='Fault deetction',
  version='0.1',
  author='jayant',
  author_email='jayantbca012@gmail.com',
  install_require=get_requirements('requirements.txt'),
  packages=find_packages()
)