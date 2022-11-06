from setuptools import setup

setup(
    name='stock-api',
    version='0.0.1',
    install_requires=[
        'django',
        'djangorestframework',
        'markdown',
        'django-filter',
        'django-environ',
        'django-cors-headers',
        'djangorestframework-simplejwt'
    ],
)