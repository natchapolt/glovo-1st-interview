"""Python setup.py for glovo_1st_interview package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("glovo_1st_interview", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="glovo_1st_interview",
    version=read("glovo_1st_interview", "VERSION"),
    description="Awesome glovo_1st_interview created by natchapolt",
    url="https://github.com/natchapolt/glovo-1st-interview/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="natchapolt",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["glovo_1st_interview = glovo_1st_interview.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
