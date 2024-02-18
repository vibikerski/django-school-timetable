from actions.base_handler import get_instance
from actions.base_handler import get_fields as fields
from validation import validate_updating


def update_subject(values):
    if err := validate_updating(values, "subject"):
        return {"error": err, "data": None}

    subject = get_instance("subject", values.get('ID'))

    if title := values.get('Title'):
        subject.title = title
    if description := values.get('Description'):
        subject.description = description

    subject.save()
    return {"error": None, "data": None}


def update_teacher(values):
    if err := validate_updating(values, "teacher"):
        return {"error": err, "data": None}

    teacher = get_instance("teacher", values.get('ID'))

    if subject_id := values.get("Subject ID"):
        subject = get_instance("subject", subject_id)
        subject.teacher_set.add(teacher)

    if name := values.get("Name"):
        teacher.name = name
    if surname := values.get("Surname"):
        teacher.surname = surname
    if birth_year := values.get("Birth Year"):
        teacher.birth_year = int(birth_year)
    if position := values.get("Position"):
        teacher.position = position

    teacher.save()
    return {"error": None, "data": None}


def update_class(values):
    if err := validate_updating(values, "class"):
        return {"error": err, "data": None}
    
    class_ = get_instance("class", values.get('ID'))

    if teacher_id := values.get("Teacher ID"):
        teacher = get_instance("teacher", teacher_id)
        class_.teacher = teacher
    if title := values.get('Title'):
        class_.title = title

    class_.save()
    return {"error": None, "data": None}


def update_student(values):
    if err := validate_updating(values, "student"):
        return {"error": err, "data": None}
    student = get_instance("student", values.get('ID'))

    if class_id := values.get('Class ID'):
        class_ = get_instance("class", class_id)
        student.study_class = class_

    if name := values.get('Name'):
        student.name = name
    if surname := values.get('Surname'):
        student.surname = surname
    if birth_year := int(values.get('Birth Year')):
        student.birth_year = birth_year

    student.save()
    return {"error": None, "data": None}


def update_grade(values):
    if err := validate_updating(values, "grade"):
        return {"error": err, "data": None}
    grade = get_instance("grade", values.get('ID'))

    if value := int(values.get('Value')):
        grade.value = value
    if date := values.get('Date'):
        grade.date = date
    if student_id := values.get('Student ID'):
        student = get_instance("student", student_id)
        grade.student = student
    if subject_id := values.get('Subject ID'):
        subject = get_instance("subject", subject_id)
        grade.subject = subject

    grade.save()
    return {"error": None, "data": None}


def update_schedule(values):
    if err := validate_updating(values, "schedule"):
        return {"error": err, "data": None}
    schedule = get_instance("schedule", values.get('ID'))

    if week_day := values.get('Week day'):
        schedule.week_day = week_day
    if start_time := values.get('Start time'):
        schedule.start_time = start_time
    if subject_id := values.get('Subject ID'):
        subject = get_instance("subject", subject_id)
        schedule.subject = subject
    if class_id := values.get('Class ID'):
        class_ = get_instance("class", class_id)
        schedule.study_class = class_
    if teacher_id := values.get('Teacher ID'):
        teacher = get_instance("teacher", teacher_id)
        schedule.teacher = teacher
        
    schedule.save()
    return {"error": None, "data": None}


def get_fields(entity):
    return fields(entity, True)
