from school_timetable.models import Subject, Teacher, Class, Student, Schedule, Grade
type_model = {
    "subject": Subject,
    "class": Class,
    "teacher": Teacher,
    "student": Student,
    "schedule": Schedule,
    "grade": Grade
}

field_model = {
    'Title': 'title',
    'Description': 'description',
    'Name': 'name',
    'Surname': 'surname',
    'Birth Year': 'birth_year',
    'Position': 'position',
    'Value': 'value',
    'Date': 'date',
    'Week day': 'week_day',
    'Start time': 'start_time'
}

def get_instance(entity_type, id):
    try:
        model = type_model.get(entity_type)
        return model.objects.get(id=id)
    except model.DoesNotExist:
        return None


def get_fields(entity, include_id=False):
    entity = entity.lower()
    fields = []
    if include_id:
        fields.append(('ID', 'IntegerField'))

    if entity == 'subject':
        fields.extend([
            ('Title', 'CharField'),
            ('Description', 'TextField')
        ])
    elif entity == 'teacher':
        fields.extend([
            ('Name', 'CharField'),
            ('Surname', 'CharField'),
            ('Birth Year', 'IntegerField'),
            ('Position', 'CharField'),
            ('Subject ID', 'IntegerField')
        ])
    elif entity == 'class':
        fields.extend([
            ('Title', 'CharField'),
            ('Teacher ID', 'IntegerField')
        ])
    elif entity == 'student':
        fields.extend([
            ('Name', 'CharField'),
            ('Surname', 'CharField'),
            ('Birth Year', 'IntegerField'),
            ('Class ID', 'IntegerField')
        ])
    elif entity == "grade":
        fields.extend([
            ('Value', 'TextField'),
            ('Date', 'DateField'),
            ('Student ID', 'IntegerField'),
            ('Subject ID', 'IntegerField')
        ])
    elif entity == "schedule":
        fields.extend([
            ('Week day', 'TextField'),
            ('Start time', 'TimeField'),
            ('Subject ID', 'IntegerField'),
            ('Class ID', 'IntegerField'),
            ('Teacher ID', 'IntegerField')
        ])
    return fields
