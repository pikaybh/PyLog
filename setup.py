from setuptools import setup, find_packages

setup(
    name="pylog",
    version="2.2.1",
    author="pikaybh",
    author_email="your_email@example.com",
    description="A customizable logging system for Python applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pikaybh/pylog",  # GitHub 주소
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
