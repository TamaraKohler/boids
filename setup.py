
from setuptools import setup, find_packages

setup(
    name = "Boids",
    version = "0.1.0",
    packages = find_packages(exclude=['\test']),
    scripts = ['scripts/animate_boids'],
    #package_data = {'Boids': ['config.yaml']},
    install_requires = ['numpy', 'matplotlib'])