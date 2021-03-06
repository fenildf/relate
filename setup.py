#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# This script (for now) is only intended to install the 'relate' content helper
# script.  relate-validate. Its use is not needed for (and unrelated to)
# deploying RELATE as a web service.

# Use 'pip install -r requirements.txt' first to install prerequisites.

setup(name="relate-courseware",
      version="2016.1",
      description="RELATE courseware",
      long_description=open("README.rst", "rt").read(),

      scripts=["bin/relate"],
      author="Andreas Kloeckner",
      url="https://github.com/inducer/relate",
      author_email="inform@tiker.net",
      license="MIT",
      packages=find_packages(exclude=['tests']),
      install_requires=[
          "django>=1.10,<2.1",
          "django-crispy-forms>=1.5.1",
          "colorama",
          "markdown",
          "dulwich",
          "pyyaml",
          "nbconvert>=5.2.1",
          "pymbolic",
          "sympy",
          ],
      package_data={
          "relate": [
              "templates/*.html",
              ],
          "course": [
              "templates/course/*.html",
              "templates/course/jinja2/*.tpl",
              ],
          },
      )
