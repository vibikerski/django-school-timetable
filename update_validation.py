from school_timetable.models import Subject, Teacher, Class, Student

class Updater:
    @staticmethod
    def update_subject(values):
        try:
            subject = Subject.objects.get(id=values['ID'])
        except:
            return {"error": "ID not found."}

        if values['Title'] and len(values['Title']) > 100:
            return {"error": "Title is too long."}
        elif values['Description'] and len(values('Description')) > 100:
            return {"error": "Description is too long."}

        if values['Title']:
            subject.title = values['Title']
        if values['Description']:
            subject.description = values['Description']
        subject.save()
        return None

    @staticmethod
    def update_teacher(values):
        try:
            teacher = Teacher.objects.get(id=values['ID'])
        except:
            return {"error": "ID not found."}

        if values['Name'] and len(values["Name"]) > 100:
            return {"error": "Name is too long."}
        elif values['Surname'] and len(values["Surname"]) > 100:
            return {"error": "Surname is too long."}
        elif values['Position'] and len(values["Position"]) > 150:
            return {"error": "Position is too long."}
        elif values["Birth Year"]:
            try:
                int(values["Birth Year"])
            except:
                return {"error": "The birth year is unprocessable."}
        if values["Subject ID"]:
            try:
                subject = Subject.objects.filter(id=values['Subject ID'])
            except:
                return {"error": "No subject ID found."}
        
        if values["Name"]:
            teacher.name = values["Name"]
        if values["Surname"]:
            teacher.surname = values["Surname"]
        if values["Birth Year"]:
            teacher.birth_year = int(values["Birth Year"])
        if values["Subject ID"]:
            subject.teacher_set.add(teacher)
        teacher.save()
        return None
    
    @staticmethod
    def update_class(values):
        try:
            class_ = Class.objects.get(id=values["ID"])
        except:
            return {"error": "ID not found."}

        if values['Title'] and len(values['Title']) > 100:
            return {"error": "Title is too long."}
        elif values["Teacher ID"]:
            try:
                teacher = Teacher.objects.filter(id=values["Teacher ID"])
            except:
                return {"error": "Teacher ID not found."}

        if values['Title']:
            class_.title = values['Title']
        if values['Teacher ID']:
            class_.teacher = teacher
        class_.save()
        return None

    @staticmethod
    def update_student(values):
        try:
            student = Student.object.get(id=values["ID"])
        except:
            return {"error": "ID not found."}
        
        if values['Name'] and len(values["Name"]) > 100:
            return {"error": "Name is too long."}
        elif values['Surname'] and len(values["Surname"]) > 100:
            return {"error": "Surname is too long."}
        elif values['Birth Year']:
            try:
                int(values['Birth Year'])
            except:
                return {"error": "The birth year is unprocessable."}
        
        if values['Class ID']:
            try:
                class_ = Class.objects.filter(id=values['Class ID'])
            except:
                return {"error": "Class ID not found."}
        
        if values['Name']:
            student.name = values['Name']
        if values['Surname']:
            student.surname = values['Surname']
        if values['Birth Year']:
            student.birth_year = int(values['Birth Year'])
        if values['Class ID']:
            student.study_class = class_

    @staticmethod
    def get_fields(entity):
        if entity == 'Subject':
            return [
                ('ID', 'IntegerField'),
                ('Title', 'CharField'),
                ('Description', 'TextField')
            ]
        elif entity == 'Teacher':
            return [
                ('ID', 'IntegerField'),
                ('Name', 'CharField'),
                ('Surname', 'CharField'),
                ('Birth Year', 'IntegerField'),
                ('Position', 'CharField'),
                ('Subject ID', 'IntegerField')
            ]
        elif entity == 'Class':
            return [
                ('ID', 'IntegerField'),
                ('Title', 'CharField'),
                ('Teacher ID', 'IntegerField')
            ]
        elif entity == 'Student':
            return [
                ('ID', 'IntegerField'),
                ('Name', 'CharField'),
                ('Surname', 'CharField'),
                ('Birth Year', 'IntegerField'),
                ('Class ID', 'IntegerField')
            ]
        return []