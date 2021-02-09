# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Lab(models.Model):
    labId = models.AutoField(db_column='labId', primary_key=True)
    studentId = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentId')
    labNum = models.IntegerField(db_column='labNum')
    filePath = models.CharField(db_column='filePath').max_length = 300
    status = models.CharField().max_length = 64
    messageId = models.IntegerField(db_column='messageId')

    class Meta:
        managed = False
        db_table = 'labs'
        unique_together = (('studentId', 'labNum'),)


class Student(models.Model):
    studentId = models.AutoField(db_column='studentId', primary_key=True)
    fullName = models.CharField(db_column='fullName').max_length = 200
    groupNum = models.CharField(db_column='groupNum').max_length = 10
    nickname = models.CharField().max_length = 100
    chatId = models.IntegerField(db_column='chatId')

    class Meta:
        managed = False
        db_table = 'students'

