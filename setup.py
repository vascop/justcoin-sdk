from setuptools import setup


setup(
    name='justcoin-sdk',
    version='0.0.5',
    packages=['justcoin',],
    license='MIT',
    description = "Python SDK for the Justcoin API",
    author = "Vasco Pinho",
    author_email = "vascogpinho@gmail.com",
    url = "https://github.com/vascop/justcoin-sdk",
    download_url = "https://github.com/vascop/justcoin-sdk/zipball/master",
    keywords = ["sdk", "justcoin", "api"],
    install_requires=[
        "requests",
    ],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet",
        ],
    long_description=open('README.rst').read(),
)
