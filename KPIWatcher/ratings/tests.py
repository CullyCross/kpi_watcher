from django.contrib.auth.models import User
from django.test import TestCase

from ratings.models import Teacher, Department, Student, Group, University, Faculty


class RatingsTestCase(TestCase):

    def setUp(self):
        u = University.objects.create(name="UnitKPI")
        f = Faculty.objects.create(name="UnitFaculty", university=u)
        d = Department.objects.create(name="UnitDepartment", faculty=f)

        t_user = User.objects.create_user(username="UnitTestTeacher",
                                     email="unitemail@teacher.net",
                                     password="Unit")
        t = Teacher.objects.create(user=t_user, department=d)
        g = Group.objects.create(name="UnitGroup", department=d)

        s_user = User.objects.create_user(username="UnitStudent",
                                     email="unitemail@student.net",
                                     password="unit")
        is_leader = True
        s = Student.objects.create(user=s_user, group=g, is_leader=is_leader)

    def test_vote_for_teacher_success(self):
        user = User.objects.get(username="UnitTestTeacher")
        teacher = Teacher.objects.get(user=user)
        user = User.objects.get(username="UnitStudent")
        student = Student.objects.get(user=user)
        self.assertEqual(teacher.vote(5, student), True)

    def test_vote_for_teacher_mark(self):
        user = User.objects.get(username="UnitTestTeacher")
        teacher = Teacher.objects.get(user=user)
        user = User.objects.get(username="UnitStudent")
        student = Student.objects.get(user=user)
        self.assertEqual(teacher.vote(-1, student), False)

    def test_vote_for_teacher_not_student(self):
        user = User.objects.get(username="UnitTestTeacher")
        teacher = Teacher.objects.get(user=user)
        self.assertEqual(teacher.vote(4, teacher), False)

    def test_vote_for_teacher_voted(self):
        user = User.objects.get(username="UnitTestTeacher")
        teacher = Teacher.objects.get(user=user)
        user = User.objects.get(username="UnitStudent")
        student = Student.objects.get(user=user)
        teacher.vote(10, student)
        self.assertEqual(teacher.vote(4, student), False)

    def test_vote_for_group(self):
        user = User.objects.get(username="UnitTestTeacher")
        teacher = Teacher.objects.get(user=user)
        g = Group.objects.get(name="UnitGroup")
        self.assertEqual(g.vote(5, teacher), True)
