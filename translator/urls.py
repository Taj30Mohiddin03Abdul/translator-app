from django.contrib import admin
from core import views
from django.urls import path
from core.views import translate_text, clear_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", translate_text, name="translate"),
    path("clear/", clear_history, name="clear_history"),
    path("talk/", views.ai_talk, name="ai_talk"),
]
