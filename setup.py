from setuptools import setup
from pathlib import Path


setup(
    name="fusionscript-stubs",
    url="https://github.com/czukowski/fusionscript-stubs",
    description="DaVinci Resolve Python API stubs",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    author="Korney Czukowski",
    author_email="carbofos@seznam.cz",
    version="19.0b1",
    package_data={"fusionscript-stubs": ['fusionscript.pyi', '__init__.pyi']},
    packages=["fusionscript-stubs"]
)
