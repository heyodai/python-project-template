from setuptools import setup, find_packages
from plugin.version import __version__

# Read in the README.md for the long description.
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        # any future dependencies
    ],
    author='Odai Athamneh',
    author_email='heyodai@gmail.com',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
)