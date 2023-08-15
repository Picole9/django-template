# is docker container
DOCKER = False

# django-debug-mode, dont use this in production!
DEBUG = True

# Example: ALLOWED_HOSTS = ['django.example.com', 'django.internal.local']
ALLOWED_HOSTS = ["*"]

# To generate a suitable key, run the following command: 'python {BASE_DIR}/generate_secret_key.py'
SECRET_KEY = 'django-insecure-(ge@m2!*btktor$^n60m7l=94qe78p=3h)0)_yau=dzb88ftlk'

# Example: CSRF_TRUSTED_ORIGINS = ['django.example.com', 'django.internal.local']
CSRF_TRUSTED_ORIGINS = ['http://localhost']

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'de-DE'
TIME_ZONE = 'CET'

# Proxy
PROXY = None
