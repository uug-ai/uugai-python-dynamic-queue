from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README", 'r') as f:
    long_description = f.read()

long_description=long_description,

setup(
   name='python-queue-reader',
   version='1.0',
   description='Queue reader for python abstracting message brokers such as RabbitMQ', 
   author='uug.ai',
   author_email='', #TODO: Add email
   packages=['python-queue-reader'],
   install_requires=requirements
)