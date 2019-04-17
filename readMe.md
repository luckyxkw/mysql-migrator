# Overview
A python command line tool for migrating MySql tables

# Pre-requisite
- Python
- My Sql connector: `python -m pip install mysql-connector`

# Known Issues
- in python 2.*, `raw_input` is used to input raw string, however in 3.* `raw_input` is merged with `input` into `input`. Thus the current script only works for python 2.*. Test has only been performed on python 2.7.
