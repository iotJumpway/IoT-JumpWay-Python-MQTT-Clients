# Setup script for installing techbubbleiotjumpwaymqtt#
# Author:   Adam Milton-Barker <adammiltonbarker@gmail.com>#
# Copyright (C) 2016 - 2017 TechBubble Technologies Limited
# For license information, see LICENSE.txt

import sys
sys.path.insert(0, 'src')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='techbubbleiotjumpwaymqtt',
    version="0.2.3",
    author='Adam Milton-Barker',
    author_email='adammiltonbarker@gmail.com',
    package_dir={'': 'src'},
	package_data={'techbubbleiotjumpwaymqtt': ['*.pem']},
    url='https://github.com/TechBubbleTechnologies/Software-Python-MQTT',
    license='Eclipse Public License v1.0',
    description='TechBubble Technologies IoT JumpWay MQTT Client for Python',
    packages=['techbubbleiotjumpwaymqtt'],
    install_requires=[
        "paho-mqtt >= 1.1",
    ],
    classifiers=[],
)