from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from web_app import views

router = routers.DefaultRouter()
router.register(r'api/iief-questionnaires', views.IiefQuestionnaireViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
