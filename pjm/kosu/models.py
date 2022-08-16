from django.contrib.auth.models import User
from django.db import models


class Position_Master(models.Model):
    """役職の単金"""

    position = models.CharField(max_length=100, unique=True, null=False)
    unit_price = models.IntegerField(null=False)

    list_display = ["position", "unit_price"]

    def __str__(self):
        return self.position


class User_Master(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position_Master, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.user.username


class Project_Master(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    start = models.DateField(null=False)
    end = models.DateField(null=False)
    order = models.CharField(max_length=100, null=False)
    order_amount = models.IntegerField(null=False)

    def __str__(self):
        return self.order + " " + self.name


class Project_Member(models.Model):
    project_id = models.ForeignKey(Project_Master, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User_Master, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.project_id.name + " " + self.user.user.username


class Man_Hours(models.Model):
    """プロジェクト開始からの累計工数"""

    user = models.ForeignKey(User_Master, on_delete=models.CASCADE, null=False)
    project_id = models.ForeignKey(Project_Master, on_delete=models.CASCADE, null=False)
    hour = models.FloatField(null=False)
    collect_date = models.DateField(null=False)
    is_ss = models.BooleanField(null=False)

    def __str__(self):
        return (
            self.project_id.order
            + " "
            + self.project_id.name
            + " "
            + self.user.user.username
            + " "
            + str(self.collect_date)
            + " "
            + str(self.hour)
            + "h"
        )
