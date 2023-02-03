from django.db import models


class CommonModel(models.Model):
    num = models.IntegerField(primary_key=True)
    title = models.TextField()
    contents = models.TextField()
    date = models.TextField()


class CommonFileModel(models.Model):
    common_num = models.ForeignKey(CommonModel, related_name='file_list', on_delete=models.CASCADE)
    file_name = models.TextField()
    file_path = models.TextField()

