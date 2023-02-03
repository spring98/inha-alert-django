from django.urls import path
from .views import hello_api, common_api, common_num_api, common_file_api

urlpatterns = [
    path('hello', hello_api),
    path('common', common_api),
    path('common/file', common_file_api),
    path('common/nums', common_num_api),
    # path('common/detail/<int:num>', common_detail_api),
    # path('common/detail/post', post_common_detail_api),
]
