from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .urls import urlpatterns

# swagger
SchemaView = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_url_pattern = [
    path("swagger/", SchemaView.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
urlpatterns.extend(swagger_url_pattern)

# debug_toolbar
debug_toolbar_url_pattern = [
    path("__debug__/", include("debug_toolbar.urls")),
]
urlpatterns.extend(debug_toolbar_url_pattern)
