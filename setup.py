# setup.py
from setuptools import setup, find_packages

setup(
    name="password-generator-demo",
    version="0.1.0",
    description="Demonstration of a Python module for generating random passwords",
    author="DevOps",
    author_email="tu.email@ejemplo.com",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    # Optional configuration
    # entry_points={
    #     "console_scripts": [
    #         "password-generator = password_generator.cli:main"
    #     ]
    # },
)
