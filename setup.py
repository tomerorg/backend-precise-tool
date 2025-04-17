
from setuptools import setup, find_packages

setup(
    name="backend-precise-tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.20.0",
    ],
    author="",
    author_email="",
    description="FastAPI based backend tool in Python",
    keywords="backend-precise-tool, python",
    url="",
)
