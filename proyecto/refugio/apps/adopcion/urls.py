
from django.conf.urls import url, include

from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
urlpatterns = [
    url('index', index_adopcion),
    url('listar', SolicitudList.as_view(), name='Solicitud_listar'),
    url('nueva', SolicitudCreate.as_view(), name='Solicitud_crear'),
    url(r'^editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='Solicitud_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name='Solicitud_eliminar'),
    
]

