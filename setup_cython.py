from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        "Main_cython.py"
    ], compiler_directives={"language_level": "3"}),
)

# python3 setup_cython.py build_ext --inplace -j 8