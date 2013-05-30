from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^edition/$', 'lp_teabot.views.edition'),
    url(r'^sample/$', 'lp_teabot.views.sample'),
    url(r'^validate_config/$', 'lp_teabot.views.validate_config'),
    url(r'^meta.json$', 'lp_teabot.views.meta_json'),
    url(r'^icon.png$', 'lp_teabot.views.icon'),
    
)




