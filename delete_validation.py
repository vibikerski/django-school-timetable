from school_timetable.models import Subject, Teacher, Class, Student
from base_handler import BaseHandler

class Deleter(BaseHandler):
    @staticmethod
    def delete_instance(model_class, values):
        error, result = BaseHandler._validate_and_get_instance(model_class, values['ID'])
        if error:
            return {"error": error, "data": None}
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
    def get_fields(entity):
        return [('ID', 'IntegerField')]