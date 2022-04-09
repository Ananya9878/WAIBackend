from rest_framework.serializers import ModelSerializer
from .models import TaskModel


class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'title','is_completed']


class TaskOnlyIdSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id']