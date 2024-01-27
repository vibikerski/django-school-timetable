from school_timetable.models import Subject, Teacher, Class, Student
from base_handler import BaseHandler

class Creator(BaseHandler):
    @staticmethod
    def create_subject(values):
        title = values['Title']
        if len(title) > 100:
            return {"error": "Title is too long.", "data": None}
        
        Subject(
            title=title,
            description=values["Description"]
        ).save()
        return {"error": None, "data": None}

    @staticmethod
    def create_teacher(values):
        error, subject = BaseHandler._validate_and_get_instance(Subject, values.get("Subject ID"))
        if error:
            return {"error": error, "data": None}

        birth_year = values.get("Birth Year")
        try:
            birth_year = int(birth_year)
        except:
            return {"error": "The birth year is unprocessable.", "data": None}
        name = values.get("Name")
        if len(name) > 100:
            return {"error": "Name is too long.", "data": None}
        surname = values.get("Surname")
        if len(surname) > 100:
            return {"error": "Surname is too long.", "data": None}
        position = values.get("Position")
        if len(position) > 150:
            return {"error": "Position is too long.", "data": None}
        
        print(name, surname, birth_year, position)

        t = Teacher(
            name=name,
            surname=surname,
            birth_year=birth_year,
            position=position,
        )
        t.save()
        subject.teacher_set.add(t)
        return {"error": None, "data": None}


    @staticmethod
    def create_class(values):
        error, teacher = BaseHandler._validate_and_get_instance(Teacher, values['Teacher ID'])
        if error:
            return {"error": error, "data": None}

        title = values.get("Title")
        if len(title) > 100:
            return {"error": "Title is too long.", "data": None}

        Class(
            title=title,
            teacher=teacher
        ).save()
        return {"error": None, "data": None}

    @staticmethod
    def create_student(values):
        error, study_class = BaseHandler._validate_and_get_instance(Class, values.get("Class ID"))
        if error:
            return {"error": "The class does not exist.", "data": None}

        birth_year = values.get("Birth Year")
        try:
            birth_year = int(birth_year)
        except:
            return {"error": "The birth year is unprocessable.", "data": None}

        name = values.get("Name", "")
        surname = values.get("Surname", "")
        if len(name) > 100:
            return {"error": "Name is too long.", "data": None}
        elif len(surname) > 100:
            return {"error": "Surname is too long.", "data": None}
        
        Student(
            name=name,
            surname=surname,
            birth_year=birth_year,
            study_class=study_class
        ).save()
        return {"error": None, "data": None}

    @staticmethod
    def get_fields(entity):
        return BaseHandler.get_fields(entity)