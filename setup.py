#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


requirements = [
    'pandas>=1.4.0,<2',
    'requests>=2.20.0,<3'
]

setup_requirements = []

test_requirements = []


setup(
    author="Peter Andorfer",
    author_email='peter.andorfer@oeaw.ac.at',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Utility functions to interact with handle.net API",
    entry_points={
        'console_scripts': [
            'acdh-handle-pyutils=acdh_handle_pyutils.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='acdh-handle-pyutils',
    name='acdh-handle-pyutils',
    packages=find_packages(include=['acdh_handle_pyutils', 'acdh_handle_pyutils.*']),
    package_data={
        module.__name__: walker(
            os.path.dirname(module.__file__),
            'files'
        ),
    },
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/acdh-oeaw/acdh-handle-pyutils',
    version='0.3.0',
    zip_safe=False,
)
