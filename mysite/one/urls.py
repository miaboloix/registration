from django.urls import path

from . import views

app_name = 'one'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/details/', views.ListView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('get_data/', views.get_data, name='data'),
	path('<int:pk>/details/get_courses/', views.get_courses, name='courses'),
	path('<int:pk>/details/get_courses/meetings/<str:course_list>', views.get_details , name='meetings'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), ]