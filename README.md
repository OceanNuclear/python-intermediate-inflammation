# Introduction

This is a template software project repository used by the [Intermediate Research Software Development Skills In Python](https://github.com/carpentries-incubator/python-intermediate-development).

## Purpose

This repository is intended to be used as a code template which is copied by learners at [Intermediate Research Software Development Skills In Python](https://github.com/carpentries-incubator/python-intermediate-development) workshops.
This can be done using the `Use this template` button towards the top right of this repo's GitHub page.

## TODOs

In a number of places, `TODO` comments indicate where code may be added during the
workshop as the necessary topics are introduced.
Each `TODO` comment should refer to a particular section of the workshop:

- `TODO(lesson-collaborative)` - refers to the lesson titled 'Collaborative Software Development'
- `TODO(lesson-robust)` - refers to the lesson titled 'Writing Robust Software'
- `TODO(lesson-design)` - refers to the lesson titles 'Software Design in Python'

## Tests

Several tests have been implemented already, some of which are currently failing.
These failing tests set out the requirements for the additional code to be implemented during the workshop.

The tests should be run using `pytest`, which will be introduced during the workshop.

## Takeaway

- Comments should answer the "why" question, and occassionally the "what" question, 
- never the "how" question, as the last one is answered by the code itself instead.
- See [this blogpost](https://www.freecodecamp.org/news/code-comments-the-good-the-bad-and-the-ugly-be9cc65fbf83/) for more details

## Lessons about python package management learnt

`python setup.py --user` # Does NOT care about venv, install in ~/.local, and will be available everywhere in your user space forever.

`pip3 install .` # install to the current by copying the directory code in ./ into the lib/site-packages/ of the venv

`pip3 install -e .` # install a text abspath link to the current directory (./) into the lib/site-packages/ of the venv. The -e stands for "editable".

