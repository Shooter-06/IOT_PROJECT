from setuptools import setup, find_packages

setup(
    name='adafruit_dht',
    version='1.5.0',
    author='Adafruit Industries',
    author_email='support@adafruit.com',
    description='Python library for reading DHT series sensors.',
    url='https://github.com/adafruit/Adafruit_Python_DHT',
    packages=find_packages(),
    install_requires=[
        'Adafruit-GPIO>=1.0.0',
        'six>=1.8.0'
    ],
)
