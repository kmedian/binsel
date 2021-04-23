from setuptools import setup
import pypandoc


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(name='binsel',
      version=get_version("binsel/__init__.py"),
      description='Feature selection for Hard Voting classifier',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/kmedian/binsel',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='Apache License 2.0',
      packages=['binsel'],
      install_requires=[
          'numpy>=1.14.5,<2',
          'korr>=0.8.2,<1'
      ],
      python_requires='>=3.6',
      zip_safe=False)
