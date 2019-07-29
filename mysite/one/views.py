from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from .forms import StudentForm, CourseForm
from .models import Course, Meeting, StudentUser
from django.contrib.auth.models import User

def get_data(request, user):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = StudentForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			student_object, created = StudentUser.objects.get_or_create(user=User.objects.filter(id=user).first())
			student_object.hopid = form.cleaned_data['hopid']
			student_object.jhed = form.cleaned_data['jhed']
			student_object.grad_year = form.cleaned_data['grad_year']
			student_object.major = form.cleaned_data['major']
			student_object.pre_health = form.cleaned_data['pre_health']
			student_object.save()
			# redirect to a new URL:
			return redirect('one:results', pk=student_object.id)
	# if a GET (or any other method) we'll create a blank form
	else:
		form = StudentForm()
	return render(request, 'one/student_info.html/', context={'user': user})

def get_results(request, pk):
	student = StudentUser.objects.filter(id=pk).first()
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
			return redirect('one:detail', pk=student.id)
	# if a GET (or any other method) we'll create a blank form
	else:
		return render(request, 'one/results.html/', context={'student': student})

def details(request, pk):
	student = StudentUser.objects.filter(id=pk).first()
	courses = Course.objects.all()
	return render(request, 'one/detail.html/', context={'student': student, 'course_list': courses})

def get_courses(request, pk):
	student = StudentUser.objects.filter(id=pk).first()
	course_string = ""
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = CourseForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			course_list = request.POST.getlist('classes')
			for id in course_list:
				course_string += str(id) + "%"
			# redirect to a new URL:
		return redirect('one:meetings', pk=student.id, course_list=course_string)

def get_details(request, pk, course_list):
	student = get_object_or_404(StudentUser, pk=pk)
	course_list = course_list.split('%')
	if request.method == 'POST':
		course_string = ""
		vacant_string = ""
		full_string = ""
		for id in course_list:
			if id != '':
				course_string += str(id) + "%"
				if Meeting.objects.filter(course=get_object_or_404(Course, pk=str(id))).exists():
					data = request.POST[id]
					print(data)
					meeting = get_object_or_404(Meeting, pk=data)
					if meeting.enrollment < meeting.max:
						vacant_string += data + "%"
						#meeting.students.add(student)
					else:
						full_string += data + "%"
						#meeting.waitlist.add(student)
		return redirect('one:register_results', pk=student.id, course_list=course_string, vacant=vacant_string, full=full_string)
	else:
		object_meetings_dict = {}
		for id in course_list:
			if id != '':
				course = get_object_or_404(Course, pk=id)
				meetings = Meeting.objects.filter(course=course)
				meetings = list(meetings)
				object_meetings_dict[course] = meetings
		context={
			'student': student,
			'meetings': object_meetings_dict
		}
		return render(request, 'one/meetings.html/', context=context)

def register_results(request, pk, course_list, vacant, full):
	student = StudentUser.objects.filter(id=pk).first()
	courses = []
	course_list = course_list.split('%')
	for id in course_list:
		if id != '':
			course = get_object_or_404(Course, pk=id)
			courses.append(course)
	vacant_meetings = []
	vacant = vacant.split('%')
	for id in vacant:
		if id != '':
			meeting = get_object_or_404(Meeting, pk=id)
			vacant_meetings.append(meeting)
	full_meetings = []
	full = full.split('%')
	for id in full:
		if id != '':
			meeting = get_object_or_404(Meeting, pk=id)
			full_meetings.append(meeting)
	context = {
		'student' : student,
		'courses': course_list,
		'vacant': vacant_meetings,
		'full': full_meetings
	}
	return render(request, 'one/register_results.html/', context=context)

def get_wait_details(request, pk, course_list):
	student = get_object_or_404(StudentUser, pk=pk)
	course_list = course_list.split(',')
	if request.method == 'POST':
		object_meetings_dict = {}
		for id in course_list:
			if id != '':
				course, created_course = Course.objects.get_or_create(id=id)
				if not created_course:
					meetings = Meeting.objects.filter(course=course)
					meetings = list(meetings)
					for meeting in meetings:
						if meeting.waitlist.filter(id=pk).exists():
							#meeting.waitlist.remove(student)
							meetings.remove(meeting)
							object_meetings_dict[course] = meetings
		context = {
			'student': student,
			'meetings': object_meetings_dict
		}
		return render(request, 'one/meetings.html/', context=context)
