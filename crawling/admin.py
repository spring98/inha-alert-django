from django.contrib import admin
from .models import CommonModel

# 관리자 페이지에서 해당 모델 관리 가능
admin.site.register(CommonModel)
