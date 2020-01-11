from setuptools import setup, find_packages, find_namespace_packages
setup(
      name='webscraper',
      version=0.1,
      author='Maciej Borkowski',
      author_email='borkowski.mac@gmail.com',
      python_requires='~=3.7',
      install_requires=('Django>=3.0', 'requests', 'bs4', 'djangorestframework', 'celery', 'redis'),
      packages=find_packages(),
)
