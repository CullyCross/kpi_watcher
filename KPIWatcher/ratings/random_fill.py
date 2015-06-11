from events.models import Event

__author__ = 'cullycross'

from ratings.models import *
from random import randint

def random_fill():
    kpi = University.objects.all().first()
    n = randint(2, 3)
    for i in range(0, n):
        f = Faculty.objects.create(name="Faculty"+str(i), university=kpi)
        print f
        n1 = randint(2, 3)
        for j in range(0, n1):
            d = Department.objects.create(name="Department"+str(i)+"->"+str(j), faculty=f)
            print d
            n2 = randint(4, 7)
            for k in range(0, n2):
                u = User.objects.create_user(username="Teacher"+str(i)+"->"+str(j)+"->"+str(k),
                                             email="email"+str(i)+"->"+str(j)+"->"+str(k)+"@teacher.net",
                                             password=str(i)+"->"+str(j)+"->"+str(k))
                t = Teacher.objects.create(user=u, department=d)
                print t
            n3 = randint(4, 7)
            for m in range(0, n3):
                g = Group.objects.create(name="Group"+str(i)+"->"+str(j)+"->"+str(m), department=d)
                print g
                n4 = randint(9, 11)
                for l in range(0, n4):
                    u = User.objects.create_user(username="Student"+str(i)+"->"+str(j)+"->"+str(m)+"->"+str(l),
                                             email="email"+str(i)+"->"+str(j)+"->"+str(m)+"->"+str(l)+"@student.net",
                                             password=str(i)+"->"+str(j)+"->"+str(m)+"->"+str(l))
                    leader = randint(0, 100)
                    if leader > 80:
                        is_leader = True
                    else:
                        is_leader = False
                    s = Student.objects.create(user=u, group=g, is_leader=is_leader)
                    print s


def create_events():
    n = randint(20, 30)
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,' \
           ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' \
           ' Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris ' \
           'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor' \
           ' in reprehenderit in voluptate velit esse cillum dolore eu' \
           ' fugiat nulla pariatur. Excepteur sint occaecat cupidatat non' \
           ' proident, sunt in culpa qui officia deserunt mollit anim id' \
           ' est laborum.'
    for i in range(0, n):
        r = randint(5, 10)
        u = User.objects.order_by('?')[:r]
        creator = u.first()
        e = Event.objects.create(creator=creator, name='Event#'+str(i), text=text)
        print e
        for user in u:
            e.subscribers.add(user)


def random_votes():
    for teacher in Teacher.objects.all():
        n = randint(7, 12)
        for student in Student.objects.order_by('?')[:n]:
            v = randint(1, 10)
            print (teacher, student, v)
            teacher.vote(v, student)


def random_votes_group():
    for group in Group.objects.all():
        n = randint(7, 12)
        for teacher in Teacher.objects.order_by('?')[:n]:
            v = randint(1, 10)
            print (group, teacher, v)
            group.vote(v, teacher)


def fuck():
    random_fill()
    create_events()
    random_votes()
    random_votes_group()