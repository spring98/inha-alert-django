from rest_framework import serializers
from .models import CommonModel, CommonFileModel


class CommonFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonFileModel
        fields = ('common_num', 'file_path', 'file_name')


class CommonSerializer(serializers.ModelSerializer):
    file_list = CommonFileSerializer(many=True, read_only=True)

    class Meta:
        model = CommonModel
        fields = ('num', 'title', 'contents', 'date', 'file_list')

