from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    # host(r'main', settings.ROOT_URLCONF, name='main'),  # <-- The `name` we used to in the `DEFAULT_HOST` setting
    # host(r'training', 'Academy.urls', name='academy'),
    # host(r'pcs', 'PersonalSecurity.urls', name='mysecurity'),
    # host(r'blog', 'Blog.urls', name='blog'),
    # host(r'api', 'Api.urls', name='api'),

#
# # testing on localhost
host(r'', settings.ROOT_URLCONF, name='main'),

host(r'training', settings.ROOT_URLCONF, name='academy'),
host(r'', settings.ROOT_URLCONF, name='account'),

host(r'pcs', settings.ROOT_URLCONF, name='mysecurity'),

host(r'blog', settings.ROOT_URLCONF, name='blog'),
)
