from school_timetable.models import Subject, Teacher, Class, Student

class Creator:
    @staticmethod
    def create_subject(values):
        if len(values["Title"])>100:
            return {"error": "Title is way too long."}
        Subject(
            title=values["Title"],
            description=values["Description"]
        )
        return None
    @staticmethod
    def create_teacher(values):
        try:
            subject = Subject.objects.get(id=values["Subject ID"])
        except:
            return {"error": "The subject does not exist."}

        try:
            int(values["Birth Year"])
        except:
            return {"error": "The birth year is unprocessable."}

        t = Teacher(
            name=values["Name"],
            surname=values["Surname"],
            birth_year=int(values["Birth Year"]),
            position=values["Position"],
        )
        t.save()
        subject.teacher_set.add(t)
        return None

    @staticmethod
    def create_class(values):
        try:
            teacher = Teacher.objects.get(id=values["Teacher ID"])
        except:
            return {"error": "The teacher does not exist."}

        Class(
            title=values["Title"],
            teacher=teacher
        ).save()
        return None

    @staticmethod
    def create_student(values):
        try:
            class_ = Class.objects.get(id=values["Class ID"])
        except:
            return {"error": "The class does not exist."}

        try:
            int(values["Birth Year"])
        except:
            return {"error": "The birth year is unprocessable."}

        Student(
            name=values["Name"],
            surname=values["Surname"],
            birth_year=int(values["Birth Year"]),
            study_class=class_
        ).save()
        return None

    @staticmethod
    def get_fields(entity):
        if entity == 'Subject':
            return [
                ('Title', 'CharField'),
                ('Description', 'TextField')
            ]
        elif entity == 'Teacher':
            return [
                ('Name', 'CharField'),
                ('Surname', 'CharField'),
                ('Birth Year', 'IntegerField'),
                ('Position', 'CharField'),
                ('Subject ID', 'IntegerField')
            ]
        elif entity == 'Class':
            return [
                ('Title', 'CharField'),
                ('Teacher ID', 'IntegerField')
            ]
        elif entity == 'Student':
            return [
                ('Name', 'CharField'),
                ('Surname', 'CharField'),
                ('Birth Year', 'IntegerField'),
                ('Class ID', 'IntegerField')
            ]
        return []