from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
   name='uugai_python_dynamic_queue',
   version='1.1.0',
   description='Queue reader for python abstracting message brokers such as RabbitMQ', 
   author='uug.ai',
   author_email='support@uug.ai',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   packages=find_packages(),
   install_requires=requirements
)