from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import dm_cw1

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dm_cw1',
    description='Coursework1 on Data Mining & Machine Learning',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/QDucasse/dm_cw1',

    # Author details
    author='Quentin Ducasse',
    author_email='qd14@hw.ac.uk',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Data Science'
        'Topic :: Scientific/Engineering :: Machine Learning',
        'Topic :: Utilities',


        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',

        'Operating System :: Apple :: OSX'
    ],

    packages=find_packages(),

    install_requires=['numpy', 'matplotlib', 'pandas','sklearn','opencv-python','seaborn','image'],

)
