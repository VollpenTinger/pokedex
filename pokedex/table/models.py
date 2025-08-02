from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    release_date = models.DateField()
    descr = models.CharField(max_length=300)
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='M',
    )
    abilities = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    TYPE_CHOICES = [
        ('GRASS', 'Grass'),
        ('FIRE', 'Fire'),
        ('WATER', 'Water'),
        ('FLYING', 'Flying'),
        ('BUG', 'Bug')
    ]
    type = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='M',
    )

    WEAKNESSES_CHOICES = [
        ('GRASS', 'Grass'),
        ('FIRE', 'Fire'),
        ('WATER', 'Water'),
        ('FLYING', 'Flying'),
        ('BUG', 'Bug')
    ]
    Weaknesses = models.CharField(
        max_length=20,
        choices=WEAKNESSES_CHOICES
    )
    


