from django.db import models

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumb = models.ImageField(upload_to="thumb_cursos")

    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    classes = models.FileField(upload_to="classes")
    course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
