from setuptools import setup, find_packages
import codecs
import os

import minibar

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="minibar",
    version=minibar.__version__,

    description="Simple text progress bar library",
    long_description=long_description,

    # The project URL.
    url='https://github.com/canassa/minibar',

    # Author details
    author='Cesar Canassa',
    author_email='cesar@canassa.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Who the project is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        # Supported Python versions.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='progressbar progress bar',
    packages=['minibar'],
)
