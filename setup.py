import sys
sys.path.insert(0, 'src')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='techbubbleiotjumpwaymqtt',
    version="0.0.1",
    author='Adam Milton-Barker',
    author_email='adammiltonbarker@gmail.com',
    package_dir={'': 'src'},
	package_data={'techbubbleiotjumpwaymqtt': ['*.pem']},
    url='https://github.com/TechBubbleTechnologies/TechBubble-Iot-JumpWay-Python-MQTT',
    license='MIT',
    description='TechBubble Technologies IoT JumpWay MQTT Client for Python',
    packages=['techbubbleiotjumpwaymqtt'],
    install_requires=[
        "paho-mqtt >= 1.1",
    ],
    classifiers=[]
)