# import null as null
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.name, self.id)

class Skill(models.Model):
    SKILL_LEVELS = [
        (1, 'Fundamental Awareness' ),
        (2, 'Novice'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Expert')
    ]
    description = models.CharField(max_length=400)
    skill_level = models.IntegerField(choices=SKILL_LEVELS)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.CharField(max_length=200, default=null)

    def __str__(self):
        return '%s %s %s ' % (self.description, self.skill_level, self.user_id)