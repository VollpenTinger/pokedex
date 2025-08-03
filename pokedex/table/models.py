from django.db import models

class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Pokemon.Status.PUBLISHED)
        )

class Pokemon(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft',
        PUBLISHED = 'PB', 'PUBLISHED'


    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',default='images.png') 
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    release_date = models.DateField()
    descr = models.CharField(max_length=300)
    status = models.CharField(
        max_length=10,
        choices=Status,
        default=Status.DRAFT
    )

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
    weaknesses = models.CharField(
        max_length=20,
        choices=WEAKNESSES_CHOICES
    )
    
    objects = models.Manager()
    published = PublishedManager()


