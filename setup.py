from distutils.core import setup
 
 
setup(
    name = "django-kickass-templatetags",
    version = __import__("kickass_templatetags").__version__,
    author = "Alex Gaynor",
    author_email = "alex.gaynor@gmail.com",
    description = "A library to make Django's template tags kick ass.",
    long_description = open("README").read(),
    license = "BSD",
    url = "http://github.com/alex/django-kickass-templatetags/",
    packages = [
        "kickass_templatetags",
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
 

