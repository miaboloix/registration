from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

def create_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account Created for {0}!'.format(username))
			user = User.objects.filter(username=username).first()
			print(user.id)
			return redirect('one:data', user=user.id)
	else:
		form = UserCreationForm()
	return render(request, 'users/create_user.html/', {'form': form})
