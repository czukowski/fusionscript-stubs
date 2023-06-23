from distutils.core import setup


setup(
    name="fusionscript-stubs",
    url="https://github.com/czukowski/fusionscript-stubs",
    author="Korney Czukowski",
    author_email="carbofos@seznam.cz",
    version="18.1.2",
    package_data={"fusionscript-stubs": ['fusionscript.pyi', '__init__.pyi']},
    packages=["fusionscript-stubs"]
)
