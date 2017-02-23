from setuptools import setup, find_packages

setup(
    name = "Boids",
    version = "0.1.0",
    description = 'Simulate flocking birds',
    author = 'Tamara Kohler',
    author_email = 'tamara.kohler.16@ucl.ac.uk',
    license = 'MIT',
    packages = find_packages(exclude=['\test']),
    include_package_data=True,
    scripts = ['scripts/animate_boids'],
    install_requires = ['numpy', 'matplotlib'])