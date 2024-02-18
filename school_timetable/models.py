from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    position = models.CharField(max_length=150)

    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Class(models.Model):
    title = models.CharField(max_length=150)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_year = models.IntegerField()

    study_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Grade(models.Model):
    value = models.IntegerField()
    date = models.DateField()

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Schedule(models.Model):
    week_day = models.TextField(100)
    start_time = models.TimeField()

    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    study_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
