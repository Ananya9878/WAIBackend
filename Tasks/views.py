from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from Tasks.models import TaskModel
from Tasks.serializers import TaskSerializer, TaskOnlyIdSerializer

# Create your views here.


class TasksView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            if id:
                try:
                    instance = TaskModel.objects.get(id=id)
                except:
                    raise Exception("There is no task at that id")
                serializers = TaskSerializer(instance, many=False)
                response = serializers.data
            else:
                instances = TaskModel.objects.all()
                serializers = TaskSerializer(instances, many=True)
                response = {
                    "tasks": serializers.data
                }
            return Response(response, status=200)
        except Exception as e:
            response = {
                "error": str(e)
            }
            return Response(response, status=404)

    def post(self, request, *args, **kwargs):
        try:
            tasks = request.data.get("tasks")
            if tasks:
                data = tasks
            else:
                data = request.data
            serializers = TaskSerializer(data=data, many=True if tasks else False)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            output = TaskOnlyIdSerializer(serializers.data, many= True if tasks else False)
            if tasks:
                response = {
                    "tasks": output.data
                }
            else:
                response = output.data
            return Response(response, status=201)
        except Exception as e:
            response = {
                "error": str(e)
            }
            return Response(response, status=400)

    def put(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            try:
                instance = TaskModel.objects.get(id=id)
            except:
                raise Exception("There is no task at that id")
            serializer = TaskSerializer(instance=instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=204)
        except Exception as e:
            response = {
                "error": str(e)
            }
            return Response(response, status=404)

    def delete(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            tasks = request.data.get("tasks")
            if id and not tasks:
                try:
                    instance = TaskModel.objects.get(id=id)
                except:
                    raise Exception("There is no task at that id")

                instance.delete()
            else:
                for i in tasks:
                    try:
                        instance = TaskModel.objects.get(id=i.get("id"))
                    except:
                        raise Exception("There is no task at that id")
                    instance.delete()
            return Response(None, status=204)
        except Exception as e:
            response = {
                "error": str(e)
            }
            return Response(response, status=404)



