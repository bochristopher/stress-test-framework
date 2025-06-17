
from setuptools import setup, find_packages

setup(
    name="reli_lab",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pyserial", "pytest", "yaml"],
    entry_points={
        'console_scripts': ['reli-lab=main:main'],
    },
)
