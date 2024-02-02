from school_timetable.models import Subject, Teacher, Class, Student
from base_handler import BaseHandler


class Getter(BaseHandler):
    @staticmethod
    def get_instance(model, val):
        err, data = BaseHandler._validate_and_get_instance(model, val['ID'])
        if err:
            return {"error": err, "data": None}
        return {"error": None, "data": data}

    @staticmethod
    def get_subject(values):
        return Getter.get_instance(Subject, values)

    @staticmethod
    def get_teacher(values):
        return Getter.get_instance(Teacher, values)

    @staticmethod
    def get_class(values):
        return Getter.get_instance(Class, values)

    @staticmethod
    def get_student(values):
        return Getter.get_instance(Student, values)

    @staticmethod
    def get_fields(entity):
        return [('ID', 'IntegerField')]
