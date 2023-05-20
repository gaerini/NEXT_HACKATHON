from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Market(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Group(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    attendance = models.BooleanField()
    member_count = models.IntegerField()
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Game(models.Model):
    TYPE_CHOICES = (
        (1, '게임 1'),
        (2, '게임 2'),
        (3, '게임 3'),
    )

    type = models.IntegerField(choices=TYPE_CHOICES)
    # 다른 필드들을 추가할 수 있습니다.

    def __str__(self):
        return f'Game {self.type}'
