import os
from setuptools import setup

setup(name='ingredient_parser',
      version=0.1,
      description='Parsing English and Swedish language ingredients into name and measure of the ingredient.',
      author='Sheraz Sharif, Nibesh Shrestha',
      author_email=', mastran.nibesh@yahoo.com',
      liscence='MIT License',
      url='https://bitbucket.org/phoodster/ingredient-parser',
      long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
      platforms=['OS Independent'],
      packages=['ingredient_parser']
      )
