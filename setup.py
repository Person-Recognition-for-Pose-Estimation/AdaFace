from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name="ada_face",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    
    py_modules=['convert', 'inference', 'net', 'train_val', 'config', 'data', 'evaluate_utils', 'head', 'utils'],
    
    license='MIT',
)
