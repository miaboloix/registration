from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from . import views

app_name = 'one'
urlpatterns = [
	path('', user_views.create_user, name='home'),
	path('signin/', user_views.create_user, name='sign_in'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	path('<int:user>/get_data/', views.get_data, name='data'),
	path('<int:pk>/results/', views.get_results, name='results'),
	path('<int:pk>/details/', views.details, name='detail'),
	path('<int:pk>/details/get_courses/', views.get_courses, name='courses'),
	path('<int:pk>/meetings/<course_list>/', views.get_details , name='meetings'),
	path('<int:pk>/meetings/<course_list>/get_details/', views.get_details , name='selected_meetings'),
	path('<int:pk>/meetings/<course_list>/<vacant>/<full>/register/', views.register_results , name='register_results'),
]