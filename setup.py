from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
   name='python_queue_reader',
   version='1.1',
   description='Queue reader for python abstracting message brokers such as RabbitMQ', 
   author='uug.ai',
   author_email='', #TODO: Add email
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   packages=find_packages(),
   install_requires=requirements
)