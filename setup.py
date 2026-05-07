from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME RECOMMENDER",
    version="0.1.0",
    author="Pradnyesh Sawant",
    packages=find_packages(),
    install_requires=requirements,
)