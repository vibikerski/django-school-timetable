from school_timetable.models import Subject, Teacher, Class, Student
from base_handler import BaseHandler

class Updater(BaseHandler):
    @staticmethod
    def update_subject(values):
        error, subject = BaseHandler._validate_and_get_instance(Subject, values.get('ID'))
        if error:
            return {"error": error}

        title = values.get('Title')
        if title and len(title) > 100:
            return {"error": "Title is too long."}

        description = values.get('Description')
        if description and len(description) > 100:
            return {"error": "Description is too long."}

        if title:
            subject.title = title
        if description:
            subject.description = description

        subject.save()
        return None

    @staticmethod
    def update_teacher(values):
        error, teacher = BaseHandler._validate_and_get_instance(Teacher, values.get('ID'))
        if error:
            return {"error": error}

        name = values.get("Name")
        if name and len(name) > 100:
            return {"error": "Name is too long."}

        surname = values.get("Surname")
        if surname and len(surname) > 100:
            return {"error": "Surname is too long."}

        position = values.get("Position")
        if position and len(position) > 150:
            return {"error": "Position is too long."}

        birth_year = values.get("Birth Year")
        if birth_year:
            try:
                birth_year = int(birth_year)
            except ValueError:
                return {"error": "The birth year is unprocessable."}

        subject_id = values.get("Subject ID")
        if subject_id:
            error, subject = BaseHandler._validate_and_get_instance(Subject, subject_id)
            if error:
                return {"error": error}
            subject.teacher_set.add(teacher)

        if name:
            teacher.name = name
        if surname:
            teacher.surname = surname
        if birth_year:
            teacher.birth_year = birth_year

        teacher.save()
        return None

    
    @staticmethod
    def update_class(values):
        error, class_ = BaseHandler._validate_and_get_instance(Class, values.get("ID"))
        if error:
            return {"error": error}

        title = values.get('Title')
        if title and len(title) > 100:
            return {"error": "Title is too long."}

        teacher_id = values.get("Teacher ID")
        if teacher_id:
            error, teacher = BaseHandler._validate_and_get_instance(Teacher, teacher_id)
            if error:
                return {"error": error}
            class_.teacher = teacher

        if title:
            class_.title = title

        class_.save()
        return None

    @staticmethod
    def update_student(values):
        error, student = BaseHandler._validate_and_get_instance(Student, values.get("ID"))
        if error:
            return {"error": error}
        
        name = values.get('Name')
        if name and len(name) > 100:
            return {"error": "Name is too long."}
        
        surname = values.get('Surname')
        if surname and len(surname) > 100:
            return {"error": "Surname is too long."}
        
        birth_year = values.get('Birth Year')
        if birth_year:
            try:
                birth_year = int(birth_year)
            except ValueError:
                return {"error": "The birth year is unprocessable."}
        
        class_id = values.get('Class ID')
        if class_id:
            error, class_ = BaseHandler._validate_and_get_instance(Class, class_id)
            if error:
                return {"error": error}
            student.study_class = class_
        
        if name:
            student.name = name
        if surname:
            student.surname = surname
        if birth_year:
            student.birth_year = birth_year
        
        student.save()
        return None

    @staticmethod
    def get_fields(entity):
        return BaseHandler.get_fields(entity, True)