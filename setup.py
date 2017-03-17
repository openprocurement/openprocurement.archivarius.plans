import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = [
    'setuptools',
    'openprocurement.archivarius.core',
]
api_requires = [
    'openprocurement.api',
    'openprocurement.planning.api',
]
test_requires = requires + api_requires + [
    'webtest',
    'python-coveralls',
    'nose',
    'mock'
]

entry_points = {
    'openprocurement.api.plugins': [
        'archivarius.plans = openprocurement.archivarius.plans:includeme'
    ],
    'openprocurement.archivarius.resources': [
        'plans = openprocurement.archivarius.plans.resource:plan_filter'
    ],
}

setup(name='openprocurement.archivarius.plans',
      version='1.0.0dev',
      description='openprocurement.archivarius.plans',
      long_description=README,
      classifiers=[
          "Framework :: Pylons",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      url='https://github.com/openprocurement/openprocurement.archivarius.plans',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openprocurement', 'openprocurement.archivarius'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=test_requires,
      extras_require={'api': api_requires, 'test': test_requires},
      test_suite="openprocurement.archivarius.plans.tests.main.suite",
      entry_points=entry_points)
