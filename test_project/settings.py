# Bare ``settings.py`` for running tests for url_filter

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'url_filter.sqlite'
    }
}

INSTALLED_APPS = (
    'test_project.many_to_many',
    'test_project.many_to_one',
    'test_project.one_to_one',

    'url_filter',

    'django_extensions',
    'rest_framework',

    'django.contrib.staticfiles',
)

STATIC_URL = '/static/'
SECRET_KEY = 'foo'

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'test_project.urls'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'url_filter.integrations.drf.DjangoFilterBackend',
    ]
}
