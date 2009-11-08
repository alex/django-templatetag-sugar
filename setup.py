from distutils.core import setup
 
 
setup(
    name = "django-templatetag-sugar",
    version = __import__("templatetag_sugar").__version__,
    author = "Alex Gaynor",
    author_email = "alex.gaynor@gmail.com",
    description = "A library to make Django's template tags sweet.",
    long_description = open("README").read(),
    license = "BSD",
    url = "http://github.com/alex/django-templatetag-sugar/",
    packages = [
        "templatetag_sugar",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
 

