from distutils.core import setup
import Cython.Build

setup(
    ext_modules=Cython.Build.cythonize("pil2epd.pyx")
)
