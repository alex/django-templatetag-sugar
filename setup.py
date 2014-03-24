from setuptools import setup


with open("README.rst") as f:
    long_description = f.read()

setup(
    name="django-templatetag-sugar",
    version=__import__("templatetag_sugar").__version__,
    author="Alex Gaynor",
    author_email="alex.gaynor@gmail.com",
    description="A library to make Django's template tags sweet.",
    long_description=long_description,
    license="BSD",
    url="http://github.com/alex/django-templatetag-sugar/",
    packages=[
        "templatetag_sugar",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
