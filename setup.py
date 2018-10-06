from setuptools import setup

setup(
    version="0.1",
    author="Sven Haardiek",
    author_email="sven@haardiek.de",
    description="Python library to override configuration entries with environment variables",  # noqa 501
    name="env2conf",
    packages=["env2conf"],
    test_suite="tests",
)
