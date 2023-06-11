import os

from setuptools import setup

requires = [
    'avral',
    'argparse',
    'shapely',
]

setup(
    name='avral_convertation',
    version='0.0.1',
    description='Convert data using Avral Convertation tool',
    classifiers=[
        "Programming Language :: Python",
    ],
    author='nextgis',
    author_email='info@nextgis.com',
    url='http://nextgis.com',
    keywords='convertation',
    packages=['avral_convertation'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'avral_operations': [
            'convert = avral_convertation.operations:Converter',
        ],
    }
)
