from setuptools import find_packages,setuptools
from typing import List

HYPHEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    requiremnts=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.read_lines()
        requiremnts=[ req.replace("\n","")for req in requiremnts]
       if HYPHEN_E_DOT in requiremnts:
        requiremnts.remove(HYPHEN_E_DOT)
    return requiremnts   



setup(
    name="RegressorProject",
    version="0.0.1",
    author="Anshu",
    authoe_email="anshusmartML@gmail.com",
    install_requires=get_requirements("requiremnts.txt"),
    packages=find_packages()
)



