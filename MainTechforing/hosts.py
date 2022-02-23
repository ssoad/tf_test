from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    # For Production
    host(r'', settings.ROOT_URLCONF, name=''),
    # <-- The `name` we used to in the `DEFAULT_HOST` setting
    # host(r'help', 'help.urls', name='help'),
    host(r'training', 'Academy.urls', name='academy'),
    host(r'pcs', 'PersonalSecurity.urls', name='mysecurity'),
    host(r'main', settings.ROOT_URLCONF, name='blog'),
    host(r'main', settings.ROOT_URLCONF, name='account'),
    host(r'main', settings.ROOT_URLCONF, name='api'),


    # For Development
    # host(r'', settings.ROOT_URLCONF, name='main'),
    # host(r'', settings.ROOT_URLCONF, name='academy'),
    # host(r'', settings.ROOT_URLCONF, name='account'),
    # host(r'', settings.ROOT_URLCONF, name='mysecurity'),
    # host(r'', settings.ROOT_URLCONF, name='blog'),
)
