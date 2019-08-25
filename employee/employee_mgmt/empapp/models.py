from django.db import models
class Employee(models.Model):
    eid = models.CharField(max_length=20, primary_key=True)
    won = models.ForeignKey(
        'WonDetails',
        on_delete=models.CASCADE,
    )
    ename = models.CharField(max_length=100)
    status = models.CharField(max_length=15)
    start_date = models.DateField(max_length=15, default=None)
    end_date = models.DateField(max_length=15, default=None)
    class Meta:
        db_table = "employee"
class WonDetails(models.Model):
    won_no = models.IntegerField(primary_key=True)
    won_name = models.CharField(max_length=100)
    class Meta:
        db_table = "won_details"