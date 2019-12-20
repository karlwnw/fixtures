
import sys, os
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
import pydoc

setup(
    name = 'fixture',
    version = '3.0',
    author = 'Kumar McMillan',
    author_email = 'kumar dot mcmillan / gmail.com',
    description = 'fixture is a python module for loading and referencing test data',
    classifiers = [ 'Environment :: Other Environment',
                    'Intended Audience :: Developers',
                    (   'License :: OSI Approved :: GNU Library or Lesser '
                        'General Public License (LGPL)'),
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python',
                    'Topic :: Software Development :: Testing',
                    'Topic :: Software Development :: Quality Assurance',
                    'Topic :: Utilities'],
    long_description = """
It provides several utilities for achieving a fixed state when testing Python programs. Specifically, these utilities setup / teardown databases and work with temporary file systems. This is useful for testing and came about to fulfill stories like these:

I want to load data into a test database and easily reference that data when making assertions.
I want data linked by foreign key to load automatically and delete without integrity error.
I want to reference linked rows by meaningful names, not hard-coded ID numbers.
I don’t want to worry about auto-incrementing sequences.
I want to recreate an environment (say, for a bug) by querying a database for real data.
I want to test with files in a temporary, transparent file system.
""",
    license = 'GNU Lesser General Public License (LGPL)',
    keywords = ('test testing tools unittest fixtures setup teardown '
                'database stubs IO tempfile'),
    url = 'http://farmdev.com/projects/fixture/',

    packages = find_packages(),

    test_suite="fixture.setup_test_not_supported",
    entry_points = {
        'console_scripts': [ 'fixture = fixture.command.generate:main' ]
        },
    # the following allows e.g. easy_install fixture[django]
    extras_require = {
        'decorators': ['nose>=0.9.2'],
        'sqlalchemy': ['SQLAlchemy>=0.4'],
        'sqlobject': ['SQLObject==0.8'],
        'django': ['django'],
        },
    )
