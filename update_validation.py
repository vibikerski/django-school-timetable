from school_timetable.models import Subject, Teacher, Class, Student
from base_handler import BaseHandler


class Updater(BaseHandler):
    @staticmethod
    def update_subject(values):
        args = (Subject, values.get('ID'))
        err, subject = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err}

        title = values.get('Title')
        if title and len(title) > 100:
            return {"error": "Title is too long.", "data": None}

        description = values.get('Description')
        if description and len(description) > 100:
            return {"error": "Description is too long.", "data": None}

        if title:
            subject.title = title
        if description:
            subject.description = description

        subject.save()
        return None

    @staticmethod
    def update_teacher(values):
        args = (Teacher, values.get('ID'))
        err, teacher = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err}

        name = values.get("Name")
        if name and len(name) > 100:
            return {"error": "Name is too long.", "data": None}

        surname = values.get("Surname")
        if surname and len(surname) > 100:
            return {"error": "Surname is too long.", "data": None}

        position = values.get("Position")
        if position and len(position) > 150:
            return {"error": "Position is too long.", "data": None}

        birth_year = values.get("Birth Year")
        if birth_year:
            try:
                birth_year = int(birth_year)
            except ValueError:
                err = "The birth year is unprocessable."
                return {"error": err, "data": None}

        subject_id = values.get("Subject ID")
        if subject_id:
            args = (Subject, subject_id)
            err, subject = BaseHandler._validate_and_get_instance(*args)
            if err:
                return {"error": err, "data": None}
            subject.teacher_set.add(teacher)

        if name:
            teacher.name = name
        if surname:
            teacher.surname = surname
        if birth_year:
            teacher.birth_year = birth_year

        teacher.save()
        return {"error": None, "data": None}

    @staticmethod
    def update_class(values):
        args = (Class, values.get("ID"))
        err, class_ = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        title = values.get('Title')
        if title and len(title) > 100:
            return {"error": "Title is too long.", "data": None}

        teacher_id = values.get("Teacher ID")
        if teacher_id:
            args = (Teacher, teacher_id)
            err, teacher = BaseHandler._validate_and_get_instance(*args)
            if err:
                return {"error": err, "data": None}
            class_.teacher = teacher

        if title:
            class_.title = title

        class_.save()
        return {"error": None, "data": None}

    @staticmethod
    def update_student(values):
        args = (Student, values.get("ID"))
        err, student = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        name = values.get('Name')
        if name and len(name) > 100:
            return {"error": "Name is too long.", "data": None}

        surname = values.get('Surname')
        if surname and len(surname) > 100:
            return {"error": "Surname is too long.", "data": None}

        birth_year = values.get('Birth Year')
        if birth_year:
            try:
                birth_year = int(birth_year)
            except ValueError:
                err = "The birth year is unprocessable."
                return {"error": err, "data": None}

        class_id = values.get('Class ID')
        if class_id:
            args = (Class, class_id)
            err, class_ = BaseHandler._validate_and_get_instance(*args)
            if err:
                return {"error": err, "data": None}
            student.study_class = class_

        if name:
            student.name = name
        if surname:
            student.surname = surname
        if birth_year:
            student.birth_year = birth_year

        student.save()
        return {"error": None, "data": None}

    @staticmethod
    def get_fields(entity):
        return BaseHandler.get_fields(entity, True)
