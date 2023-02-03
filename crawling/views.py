from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CommonModel
from .serializers import CommonSerializer, CommonFileSerializer
from rest_framework import status
from django.core.paginator import Paginator


@api_view(['GET'])
def hello_api(request):
    return Response('hello world!')


@api_view(['GET', 'POST'])
def common_api(request):
    if request.method == 'GET':
        '''
            data = CommonModel.objects.all().order_by('-num')
            serializer = CommonSerializer(data, many=True)
            return Response(serializer.data)
        '''

        commons = CommonModel.objects.all().order_by('-num')
        page = int(request.GET.get('p', 1))
        # p라는 값으로 받을거고, 없으면 첫번째 페이지로
        paginator = Paginator(commons, 10)
        # Paginator 함수를 적용하는데, 첫번째 인자는 위에 변수인 전체 오브젝트, 2번째 인자는
        # 한 페이지당 오브젝트 2개씩 나오게 설정
        specific_common = paginator.get_page(page)
        # 처음 2개가 세팅 된다.
        serializer = CommonSerializer(specific_common, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def common_file_api(request):
    serializer = CommonFileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def common_num_api(request):
    count = CommonModel.objects.count()

    return_data = {
        'nums': count
    }
    return Response(return_data)

