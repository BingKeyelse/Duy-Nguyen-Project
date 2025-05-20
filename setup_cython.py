from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        "Main.py"
        # "icons_rc.py", 
        # "main_gui.py", 
        # "ui_effect_gui.py",
        # "import_all.py",
        # "auto_tranfer_file.py"
    ], compiler_directives={"language_level": "3"}),
)

# python setup_cython.py build_ext --inplace -j 8