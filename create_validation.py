from school_timetable.models import Subject, Teacher, Class, Student, Schedule, Grade
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
        args = (Subject, values.get("Subject ID"))
        err, subject = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        birth_year = values.get("Birth Year")
        try:
            birth_year = int(birth_year)
        except ValueError:
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
        args = (Teacher, values['Teacher ID'])
        err, teacher = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        title = values.get("Title")
        if len(title) > 100:
            return {"error": "Title is too long.", "data": None}

        Class(
            title=title,
            teacher=teacher
        ).save()
        return {"error": None, "data": None}

    @staticmethod
    def create_student(vals):
        args = (Class, vals.get("Class ID"))
        err, study_class = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        birth_year = vals.get("Birth Year")
        try:
            birth_year = int(birth_year)
        except ValueError:
            return {"error": "The birth year is unprocessable.", "data": None}

        name = vals.get("Name", "")
        surname = vals.get("Surname", "")
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
    def create_grade(vals):
        args = (Student, vals.get("Student ID"))
        err, student = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        args = (Subject, vals.get("Subject ID"))
        err, subject = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        value = vals['Value']
        try:
            value = int(value)
        except ValueError:
            return {
                "error": "Cannot process the grade.",
                "data": None
            }

        if value < 0:
            return {
                "error": "Cannot process the grade.",
                "data": None
            }

        Grade(
            value=value,
            date=vals['Date'],
            student=student,
            subject=subject
        ).save()
        return {"error": None, "data": None}

    @staticmethod
    def create_schedule(vals):
        args = (Subject, vals.get("Subject ID"))
        err, subject = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        args = (Class, vals.get('Class ID'))
        err, study_class = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        args = (Teacher, vals.get('Teacher ID'))
        err, teacher = BaseHandler._validate_and_get_instance(*args)
        if err:
            return {"error": err, "data": None}

        Schedule(
            week_day=vals.get('Week day'),
            start_time=vals.get('Start time'),
            subject=subject,
            study_class=study_class,
            teacher=teacher
        ).save()
        return {"error": None, "data": None}

    @staticmethod
    def get_fields(entity):
        return BaseHandler.get_fields(entity)
