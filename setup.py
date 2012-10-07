from setuptools import setup, find_packages
import os

version = '0.1.dev0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.rst')
    + '\n' +
    read('CONTRIBUTORS.rst')
    + '\n'
    )

setup(name='roald.theme',
      version=version,
      description="Theming for Sailtraining.de",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        ],
      keywords='',
      author='Wolfgang Thomas',
      author_email='thomasw@gmx.org',
      url='https://github.com/syslabcom/roald.theme',
      license='gpl',
      packages=['roald', 'roald/theme'],
      package_dir = {'': 'src'},
      namespace_packages=['roald'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
