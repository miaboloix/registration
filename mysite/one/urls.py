from django.urls import path
from . import views

app_name = 'one'
urlpatterns = [
	path('<int:user>/get_data/', views.get_data, name='data'),
	path('<int:pk>/results/', views.get_results, name='results'),
	path('<int:pk>/details/', views.details, name='detail'),
	path('<int:pk>/details/get_courses/', views.get_courses, name='courses'),
	path('<int:pk>/meetings/<course_list>/', views.get_details , name='meetings'),
	path('<int:pk>/meetings/<course_list>/get_details/', views.get_details , name='selected_meetings'),
	path('<int:pk>/meetings/<course_list>/<vacant>/<full>/register/', views.register_results , name='register_results'),
]