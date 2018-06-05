from django.db import models

# Create your models here.
class User(models.Model):
    account = models.CharField(max_length = 20, primary_key=True)
    pswd = models.CharField(max_length = 30)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.account


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    publisher = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)
    describe = models.TextField()
    start = models.DateTimeField()
    period = models.IntegerField()
    cost = models.IntegerField()
    receiver = models.CharField(max_length = 20)
    status = models.IntegerField() # %
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' ' + self.name

