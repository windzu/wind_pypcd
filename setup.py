"""
Author: wind windzu1@gmail.com
Date: 2023-08-25 17:16:49
LastEditors: wind windzu1@gmail.com
LastEditTime: 2023-08-25 17:27:23
Description: 
Copyright (c) 2023 by windzu, All Rights Reserved. 
"""
import os

from setuptools import setup

# Get version and release info, which is all stored in pypcd/version.py
ver_file = os.path.join("pypcd", "version.py")
with open(ver_file) as f:
    exec(f.read())

opts = dict(
    name=NAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    download_url=DOWNLOAD_URL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    platforms=PLATFORMS,
    version=VERSION,
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    install_requires=INSTALL_REQUIRES,
)


if __name__ == "__main__":
    setup(**opts)
