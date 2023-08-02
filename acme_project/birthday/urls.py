# birthday/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.urls import include
app_name = 'birthday'

urlpatterns = [
    path('', views.BirthdayCreateView.as_view(), name='create'),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/',
         views.BirthdayDeleteView.as_view(),
         name='delete'),
    path('login_only/', views.simple_view),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
