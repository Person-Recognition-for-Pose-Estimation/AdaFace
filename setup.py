from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name="ada-face",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    
    # Choose your license
    license='MIT',
)
