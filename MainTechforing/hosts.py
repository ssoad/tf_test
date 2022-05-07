from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    # For Production
    # host(r'main', settings.ROOT_URLCONF, name='main'), # <-- Change it to host(r'', settings.ROOT_URLCONF, name='')
    host(r'root', settings.ROOT_URLCONF, name='main'), # <-- Change it to host(r'', settings.ROOT_URLCONF, name='')
    # <-- The `name` we used to in the `DEFAULT_HOST` setting
    # host(r'help', 'help.urls', name='help'),
    host(r'school', 'Academy.urls', name='academy'),
    # host(r'pcs', 'PersonalSecurity.urls', name='mysecurity'),
    host(r'consumer', 'PersonalSecurity.urls', name='mysecurity'),
    # host(r'main', settings.ROOT_URLCONF, name='blog'), # <-- Change it to host(r'blog', settings.ROOT_URLCONF, name='blog')
    host(r'blog', settings.ROOT_URLCONF, name='blog'), # <-- Change it to host(r'blog', settings.ROOT_URLCONF, name='blog')
    host(r'root', settings.ROOT_URLCONF, name='account'),
    host(r'root', settings.ROOT_URLCONF, name='api'),


    # For Development
    # host(r'', settings.ROOT_URLCONF, name='main'),
    # host(r'', settings.ROOT_URLCONF, name='academy'),
    # host(r'', settings.ROOT_URLCONF, name='account'),
    # host(r'', settings.ROOT_URLCONF, name='mysecurity'),
    # host(r'', settings.ROOT_URLCONF, name='blog'),
)
