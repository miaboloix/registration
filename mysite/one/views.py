from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from .forms import StudentForm, CourseForm
from .models import Choice, Question, Student, Course, Meeting

class DetailView(generic.DetailView):
	model = Meeting
	template_name = 'one/meetings.html'

class IndexView(generic.ListView):
	template_name = 'one/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class ListView(generic.ListView):
	template_name = 'one/detail.html'
	context_object_name = 'course_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Course.objects.all()


class ResultsView(generic.DetailView):
	model = Student
	template_name = 'one/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'one/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('one:results', args=(question.id,)))

def get_courses(request, pk):
	student = Student.objects.filter(id=pk)
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = CourseForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			course_list = request.POST.getlist('classes')
			string = ""
			for id in course_list:
			    string += str(id)
			    string += ','
			# redirect to a new URL:
			return HttpResponseRedirect('meetings/' + string)
	     # if a GET (or any other method) we'll create a blank form
	else:
		form = CourseForm()
		return render(request, 'one/detail.html', {'form': form})

def get_details(request, pk, course_list):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = StudentForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			#
			# redirect to a new URL:
			return HttpResponseRedirect(reverse('one:results', args=(student_object.id,)))
	# if a GET (or any other method) we'll create a blank form 
	else:
		student = Student.objects.filter(id=pk)
		return render(request, 'meetings.html', {'student': student})

def get_data(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = StudentForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			new_hopid = form.cleaned_data['hopid']
			student_object, created = Student.objects.get_or_create(hopid=new_hopid)
			student_object.jhed = form.cleaned_data['jhed']
			student_object.grad_year = form.cleaned_data['grad_year']
			student_object.major = form.cleaned_data['major']
			student_object.pre_health = form.cleaned_data['pre_health']
			student_object.save()
			# redirect to a new URL:
			return HttpResponseRedirect(reverse('one:results', args=(student_object.id,)))
	# if a GET (or any other method) we'll create a blank form
	else:
		form = StudentForm()
		return render(request, 'index.html', {'form': form})