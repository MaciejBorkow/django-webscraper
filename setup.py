from setuptools import setup, find_packages
setup(
      name='webscrapermaciej',
      version=0.1,
      packages=find_packages(),
      install_requires=('Django>=3.0', 'requests', 'bs4', 'djangorestframework', 'celery', 'redis'),
)
