from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    # ex: /core/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /core/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /core/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /core/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]
