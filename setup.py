import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huelights",
    version="0.0.1",
    author="Zack Elia",
    author_email="pypi@zacharyelia.com",
    description="A Python wrapper to interact with Philips Hue smart lights",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zackelia/huelights",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
