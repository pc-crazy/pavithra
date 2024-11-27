from django.utils.timezone import now
from rest_framework import response, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from task.models import *
# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework import  serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"



class TaskCreateListApiView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        qs = super(TaskCreateListApiView, self, ).get_queryset()
        status = self.request.query_params.get('status')
        if status and status.upper() == 'PENDING':
            qs.filter(status=0)
        if status and status.upper() == 'COMPLETED':
            qs.filter(status=1)
        return qs

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # if not serializer.validated_data['due_date']:
        #     raise ValidationError("please add due date")
        #
        # if not serializer.validated_data['due_date'] > now():
        #     raise ValidationError("please add future data in due date")

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)