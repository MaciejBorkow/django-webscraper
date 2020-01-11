from setuptools import setup, find_packages, find_namespace_packages
setup(
      name='webscraper',
      version=0.1,
      packages=find_namespace_packages('webscraper', 'webscraper.*'),
      install_requires=('Django>=3.0', 'requests', 'bs4', 'djangorestframework', 'celery', 'redis'),
)
