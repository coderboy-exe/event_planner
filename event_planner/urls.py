"""event_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from listings.views import (
    all_listings,
    get_listing,
    create_listing,
    update_listing,
    delete_listing
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_listings),
    path('listings/<id>/', get_listing),
    path('listings/<id>/edit/', update_listing),
    path('listings/<id>/delete/', delete_listing),
    path('add-listing/', create_listing),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)