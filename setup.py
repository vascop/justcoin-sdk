from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()


setup(
    name='justcoin-sdk',
    version='0.0.3',
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
    long_description=read_md('README.md'),
)
