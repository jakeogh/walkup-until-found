# -*- coding: utf-8 -*-

import sys
from setuptools import find_packages, setup
if not sys.version_info[0] == 3:
    sys.exit("Python 3 is required. Use: \'python3 setup.py install\'")

dependencies = ["icecream", "click", "colorama"]

config = {
    "version": "0.1",
    "name": "walkup-until-found",
    "url": "https://github.com/jakeogh/walkup-until-found",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "Short explination of what it does _here_",
    "long_description": __doc__,
    "packages": find_packages(exclude=['tests']),
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
    "entry_points": {
        "console_scripts": [
            "walkup-until-found=walkup_until_found.walkup_until_found:cli",
        ],
    },
}

setup(**config)
