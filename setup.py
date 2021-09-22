from setuptools import setup, find_packages, find_namespace_packages

setup(
    extras_require={
        "dev": [
            "appdirs==1.4.3",
            "attrs==19.3.0",
            "backcall==0.1.0",
            "black==19.10b0; python_version >= '3.6'",
            "cached-property==1.5.1",
            "cerberus==1.3.2",
            "certifi==2019.11.28",
            "chardet==3.0.4",
            "click==7.0",
            "colorama==0.4.1",
            "decorator==4.4.1",
            "distlib==0.3.0",
            "first==2.0.2",
            "idna==2.8",
            "importlib-metadata==1.4.0; python_version < '3.8'",
            "ipython==7.11.1",
            "ipython-genutils==0.2.0",
            "jedi==0.15.2",
            "more-itertools==8.1.0",
            "orderedmultidict==1.0.1",
            "packaging==19.2",
            "parso==0.5.2",
            "pathspec==0.7.0",
            "pep517==0.8.1",
            "pexpect==4.7.0; sys_platform != 'win32'",
            "pickleshare==0.7.5",
            "pip-shims==0.4.0",
            "pipenv==2018.11.26",
            "pipenv-setup==2.2.5",
            "pipfile==0.0.2",
            "plette[validation]==0.2.3",
            "prompt-toolkit==3.0.2",
            "ptyprocess==0.6.0",
            "pygments==2.5.2",
            "pyparsing==2.4.6",
            "regex==2020.1.8",
            "requests==2.22.0",
            "requirementslib==1.5.3",
            "six==1.13.0",
            "toml==0.10.0",
            "tomlkit==0.5.8",
            "traitlets==4.3.3",
            "typed-ast==1.4.0",
            "typing==3.7.4.1",
            "urllib3==1.25.7",
            "virtualenv==16.7.9",
            "virtualenv-clone==0.5.3",
            "vistir==0.4.3",
            "wcwidth==0.1.8",
            "wheel==0.33.6",
            "zipp==0.6.0",
        ]
    },
    name="webscraper",
    version=0.1,
    author="Maciej Borkowski",
    author_email="borkowski.mac@gmail.com",
    python_requires="~=3.7",
    # install_requires=('Django>=3.0', 'requests', 'bs4', 'djangorestframework', 'celery', 'redis'),
    install_requires=[
        "amqp==2.5.2",
        "asgiref==3.2.3",
        "beautifulsoup4==4.8.2",
        "billiard==3.6.1.0",
        "bs4==0.0.1",
        "celery==4.4.0",
        "certifi==2019.11.28",
        "chardet==3.0.4",
        "django==3.1.13",
        "djangorestframework==3.11.0",
        "idna==2.8",
        "importlib-metadata==1.4.0; python_version < '3.8'",
        "kombu==4.6.7",
        "more-itertools==8.1.0",
        "pytz==2019.3",
        "redis==3.3.11",
        "requests==2.22.0",
        "soupsieve==1.9.5",
        "sqlparse==0.3.0",
        "urllib3==1.25.7",
        "vine==1.3.0",
        "zipp==0.6.0",
    ],
    packages=find_namespace_packages(),
    package_data={"webscraper": ["templates/webscraper/*.html"]}
    # package_data={'webscraper':['*.html']},
)
