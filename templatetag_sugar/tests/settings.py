SECRET_KEY = b"a"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = [
    "templatetag_sugar",
    "templatetag_sugar.tests",
]
