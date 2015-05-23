from django.db import models
from django.contrib.auth.models import User


class University(models.Model):
	name = models.CharField(max_length=50)
	avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, editable=False)

	def count_rating(self):
		total = 0
		for faculty in self.faculties.all():
			faculty.count_rating()
			total += faculty.avg_rating
		self.avg_rating = total / len(self.faculties.all())
		self.save()

	def __str__(self):
		return self.name


class Faculty(models.Model):
	name = models.CharField(max_length=50)
	university = models.ForeignKey(University, related_name="faculties")
	avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, editable=False)

	def count_rating(self):
		total = 0
		for department in self.departments.all():
			department.count_rating()
			total += department.avg_rating
		self.avg_rating = total / len(self.departments.all())
		self.save()


	def __str__(self):
		return self.name


class Department(models.Model):
	name = models.CharField(max_length=50)
	faculty = models.ForeignKey(Faculty, related_name="departments")
	avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, editable=False)

	def count_rating(self):
		total = 0
		for teacher in self.teachers.all():
			total += teacher.avg_rating

		for group in self.groups.all():
			total += group.avg_rating

		self.avg_rating = total / (len(self.groups.all()) + len(self.teachers.all()))
		self.save()

	def __str__(self):
		return self.name


class Teacher(models.Model):
	user = models.OneToOneField(User)
	department = models.ForeignKey(Department, related_name="teachers")
	avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, editable=False)
	count_of_votes = models.IntegerField(default=0, editable=False)

	voted_students = models.ManyToManyField('Student', related_name="rated_teachers", editable=False)

	def vote(self, vote, student):
		#if not self.voted_students.filter(student=student).exists():
		self.avg_rating = ((self.avg_rating * self.count_of_votes) + vote) / (self.count_of_votes + 1)
		self.count_of_votes += 1
		#self.voted_students.add(student)
		self.save()
		#	return True
		#else:
		#	return False

	def __str__(self):
		return self.user.get_username()


class Group(models.Model):
	name = models.CharField(max_length=50)
	department = models.ForeignKey(Department, related_name="groups")
	avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, editable=False)
	count_of_votes = models.IntegerField(default=0, editable=False)

	voted_teachers = models.ManyToManyField('Teacher', related_name="rated_groups", editable=False)

	def vote(self, vote, teacher):
		if not self.voted_teachers.filter(teacher=teacher).exists():
			self.avg_rating = ((self.avg_rating * self.count_of_votes) + vote) / (self.count_of_votes + 1)
			self.count_of_votes += 1
			self.voted_teachers.add(teacher)
			self.save()
			return True
		else:
			return False

	def __str__(self):
		return self.name


class Student(models.Model):
	user = models.OneToOneField(User)
	group = models.ForeignKey('Group', related_name="students")
	is_leader = models.BooleanField(default=False)

	def __str__(self):
		return self.user.get_username()
