from school_timetable.models import Subject, Teacher, Class, Student, Grade, Schedule
from base_handler import BaseHandler


class Deleter(BaseHandler):
    @staticmethod
    def delete_instance(model_class, values):
        args = (model_class, values['ID'])
        err, result = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}
        result.delete()
        return {"error": None, "data": None}

    @staticmethod
    def delete_subject(values):
        return Deleter.delete_instance(Subject, values)

    @staticmethod
    def delete_teacher(values):
        return Deleter.delete_instance(Teacher, values)

    @staticmethod
    def delete_class(values):
        return Deleter.delete_instance(Class, values)

    @staticmethod
    def delete_student(values):
        return Deleter.delete_instance(Student, values)

    @staticmethod
    def delete_grade(values):
        return Deleter.delete_instance(Grade, values)

    @staticmethod
    def delete_schedule(values):
        return Deleter.delete_instance(Schedule, values)

    @staticmethod
    def get_fields(entity):
        return [('ID', 'IntegerField')]
