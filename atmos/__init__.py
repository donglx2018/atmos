# -*- coding: utf-8 -*-
'''
*****
atmos
*****
---------------------------------------
An atmospheric sciences utility library
---------------------------------------

**atmos** is a library of Python programming utilities for the atmospheric
sciences. It is in ongoing development. If you have an idea for a feature or
have found a bug, please post it on the `GitHub issue tracker`_.

Information on how to use the module can be found predominantly by using the
built-in help() function in Python. Many docstrings are automatically
generated by the module and so information may appear to be missing in the
source code. HTML documentation will be available at a later date.

This module is currently alpha. The API of components at the base module
level should stay backwards-compatible, but sub-modules are subject to change.
In particular, features in the util module are likely to be changed or removed
entirely.
'''
__all__ = ["solve"]
from atmos.solve import calculate, FluidSolver
