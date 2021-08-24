import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="embed-templator",
    version="1.0.3",
    description=(
        "A Python Template manager for your discord bot to keep your embeds"
        " simple & consistent. "
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Sigmanificient/Embed-Templator",
    author="Sigmanificient",
    author_email="edhyjox@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=['embed_templator'],  # Pkg name
    include_package_data=True,
    install_requires=['discord.py']
)
