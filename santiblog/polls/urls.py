# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from .import views
urlpatterns = [
                      url(r'^$', 'polls.views.verhome', name='index' ),
                       url(r'^Curriculum/$', 'polls.views.vercv', name='Curriculum' ),
                       url(r'^Botonmagico/$', 'polls.views.verbtnmg', name='Boton' ),
                       url(r'^Calculadora/$', 'polls.views.vercal', name='Calculadora' ),
                       url(r'^Contactos/$', 'polls.views.vercon', name='Contacto' ),
                       url(r'^Conversor/$', 'polls.views.verconv', name='Conversor' ),
                       url(r'^Cronometro/$', 'polls.views.vercro', name='Cronometro' ),
                       url(r'^Barra/$', 'polls.views.verimagen', name='Barra' ),
                       url(r'^Noticias/$', 'polls.views.vernoticias', name='Noticias' ),
                       url(r'^ver_post/(?P<id_post>[0-9]+)$', 'polls.views.ver_post', name='ver_post'),
                       url(r'^save_message/$', 'polls.views.save_message', name='save_message'),
                       url(r'^contact/$', 'polls.views.contact', name='contact'),
                       url(r'^categoria/(?P<categoria>[0-9]+)$', 'polls.views.categoria', name='categoria'),
]
