"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, PollView, PollCreateView, PollDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/add', PollCreateView.as_view(), name='poll_create'),
    # path('poll/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('poll/<int:pk>/delete', PollDeleteView.as_view(), name='poll_delete'),

    # path('tasks/', TaskListView.as_view(), name='task_list'),
    # path('project/<int:pk>/tasks/add/', TaskCreateView.as_view(), name='task_create'),
    # path('tasks/<int:pk>/', TaskView.as_view(), name='task_view'),
    # path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    # path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
]
