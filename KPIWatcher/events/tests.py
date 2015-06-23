from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from events.models import Event
from ratings.models import University, Department, Faculty, Teacher, Group, Student


class EventTestCase(TestCase):

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
        e = Event.objects.create(creator=t_user, name='UnitEvent', text="UnitTestText")


    def test_subscribe_failed(self):
        s_user = User.objects.get(username="UnitStudent")
        e = Event.objects.get(name="UnitEvent")
        e.subscribe(s_user)
        self.assertEqual(e.subscribe(s_user), False)

    def test_subscribe(self):
        s_user = User.objects.get(username="UnitStudent")
        e = Event.objects.get(name="UnitEvent")
        self.assertEqual(e.subscribe(s_user), True)

    def test_unsubscribe_failed(self):
        s_user = User.objects.get(username="UnitStudent")
        e = Event.objects.get(name="UnitEvent")
        self.assertEqual(e.unsubscribe(s_user), False)

    def test_unsubscribe(self):
        s_user = User.objects.get(username="UnitStudent")
        e = Event.objects.get(name="UnitEvent")
        e.subscribe(s_user)
        self.assertEqual(e.unsubscribe(s_user), True)

    def test_is_subscribed(self):
        s_user = User.objects.get(username="UnitStudent")
        e = Event.objects.get(name="UnitEvent")
        e.subscribe(s_user)
        self.assertEqual(e.is_subscribed(s_user), True)

    def test_is_not_subscribed(self):
        s_user = User.objects.get(username="UnitStudent")
        e = Event.objects.get(name="UnitEvent")
        self.assertEqual(e.is_subscribed(s_user), False)
