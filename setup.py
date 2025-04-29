from setuptools import setup, find_packages
import os
print(r"""
     __  __  __   ____  ____   __  __ 
    / / / / / /  / ___|| ___| |  \/  |
   / / / / / /  | |    |___ \ | |\/| |
  / / / / / /   | |___  ___) || |  | |
 /_/ /_/ /_/     \____||____/ |_|  |_|
              
""")
if os.path.exists("README.md"):
    long_desc = open("README.md").read()
else:
    long_desc = "Default description"
setup(
    name="Embedded_config",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "RPi.GPIO"
    ],
    author="Bidyadhar Muduli",
    description="A package for embedded system input, output, and PI info",
    long_description= long_desc,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
