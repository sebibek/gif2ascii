from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello world app',
    ext_modules=cythonize("gif2ascii_cy.pyx", language_level = "3"),
    zip_safe=False,
)