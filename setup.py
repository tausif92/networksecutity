from setuptools import find_packages, setup


def get_requirements():
    '''
    This function will return the requirements in the list.
    Requirements are picked from requirements.txt
    '''
    try:
        requirements_list = []
        with open('requirements.txt', 'r') as fileobj:
            lines = fileobj.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
        return requirements_list
    except FileNotFoundError:
        print('requirements.txt is not found')


setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Tausif Bajaria',
    author_email='tausif@bajaria.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
