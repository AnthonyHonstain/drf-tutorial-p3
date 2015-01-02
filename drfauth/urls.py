from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('drfauth.views',
    # I am not sure if I have made the right choice for supporting angularjs ngResource and trailing slashes
    # http://stackoverflow.com/questions/16782700/django-angularjs-resource-ajax-post-500-internal-server-error
    # Notice I have started trimming off the trailing slash (I also added support in settings.py).
    #    I am going to try making the slash optional in the regex, since I can't seem to peg down
    #    consitence behavior from the trailing slash in my version of angular.
    url(r'^register[/]?$', 'register'),
    url(r'^login[/]?$', 'login'),
    url(r'^logout[/]?$', 'logout'),
    url(r'^account_status[/]?$', 'account_status'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
