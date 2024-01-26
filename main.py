import django_setup
from school_timetable.models import Subject, Teacher, Class, Student
from interface import run_interface

if __name__ == '__main__':
    run_interface()