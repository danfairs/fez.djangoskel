from setuptools import setup, find_packages
import os

version = '0.2.0'

setup(name='fez.djangoskel',
      version=version,
      description="Paster templates for creating Django applications as eggs",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Framework :: Paste",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Framework :: Django",
        ],
      keywords='',
      author='Dan Fairs',
      author_email='dan@fezconsulting.com',
      url='http://www.fezconsulting.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fez'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript>=1.3',
          'Cheetah',
      ],
      entry_points="""
      [paste.paster_create_template]
      django_app=fez.djangoskel.pastertemplates:DjangoAppTemplate
      django_project=fez.djangoskel.pastertemplates:DjangoProjectTemplate
      django_namespace_app=fez.djangoskel.pastertemplates:DjangoNamespaceAppTemplate
      django_namespace_project=fez.djangoskel.pastertemplates:DjangoNamespaceProjectTemplate
      """,
      )
