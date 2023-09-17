import uuid

from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


class Course(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False)
    name = models.CharField(max_length=255,
                            validators=[MinLengthValidator(3)],
                            unique=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Chapter(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False)
    # Numbers of chapters are whole integers
    number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    title = models.CharField(max_length=255,
                             validators=[MinLengthValidator(3)])
    course = models.ForeignKey('core.Course',
                               on_delete=models.CASCADE,
                               related_name='chapters')
    introduction = models.TextField(validators=[MinLengthValidator(20)])
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('course', 'number'),
            ('course', 'title')
        )

    def __str__(self) -> str:
        return self.title


class Section(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False)
    number = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 validators=[MinValueValidator(1.1)])
    title = models.CharField(max_length=255,
                             validators=[MinLengthValidator(3)])
    chapter = models.ForeignKey('core.Chapter',
                                on_delete=models.CASCADE,
                                related_name='sections')
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('chapter', 'number'),
            ('chapter', 'title')
        )

    def __str__(self) -> str:
        return self.title
