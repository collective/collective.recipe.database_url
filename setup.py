from setuptools import find_packages
from setuptools import setup

VERSION='0.0.1'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[],
    description='',
    entry_points={
    },
    keywords='',
    include_package_data=True,
    install_requires=[
        'dj-database-url',
    ],
    long_description=open('README.rst').read() + '\n' + open('CHANGES.rst').read(),
    name='collective.recipe.database_url',
    namespace_packages=[
        'collective',
        'collective.recipe',
    ],
    packages=find_packages(),
    url='',
    version=VERSION,
    zip_safe=False,
)