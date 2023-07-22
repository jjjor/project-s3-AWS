from django.shortcuts import redirect
from django.urls import reverse
from rest_framework import viewsets
from .serializers import *
from .models import Dog
from Project_s3.settings import (
    AWS_ACCESS_KEY_ID,
    AWS_S3_REGION_NAME,
    AWS_SECRET_ACCESS_KEY,
    URL_SQS,
)
import boto3
import uuid

"""classe responsavel pelo index, e retornar o contexto"""
sqs = boto3.client(
    "sqs",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="sa-east-1",
)


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def send_message(self, message_body, message_group_id):
        sqs.send_message(
            QueueUrl=URL_SQS,
            MessageBody=message_body,
            MessageGroupId=message_group_id,
            MessageDeduplicationId=str(uuid.uuid4()),
        )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            filme_criado = response.data
            titulo_do_filme = filme_criado["titulo"]
            message = f"O filme {titulo_do_filme} foi criado com sucesso :)"
            self.send_message(message, titulo_do_filme)
            return redirect(reverse("index"))
        return response
