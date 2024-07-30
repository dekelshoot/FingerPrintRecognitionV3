from core.views import PrintView
from django.urls import path

app_name = "core"

urlpatterns = [
    path("print", PrintView.as_view(), name = "print")
]