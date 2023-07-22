from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import *
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .viewsSet import sqs
from Project_s3.settings import URL_SQS


class IndexView(TemplateView):
    template_name = "index.html"
    success_url = reverse_lazy("index")

    # def extract_messages_from_response(self, response):
    #     messages = []
    #     if "Messages" in response:
    #         messages = [message["Body"] for message in response["Messages"]]
    #         print("Message: ", messages)
    #         for message in response["Messages"]:
    #             receipt_handle = message["ReceiptHandle"]
    #             self.delete_message(receipt_handle)
    #     return messages

    # def delete_message(self, receipt_handle):
    #     sqs.delete_message(QueueUrl=URL_SQS, ReceiptHandle=receipt_handle)
    #     print("Message deleted")

    # def retrieve_sqs_messages(self):
    #     response = sqs.receive_message(
    #         QueueUrl=URL_SQS, MaxNumberOfMessages=10)
    #     messages = self.extract_messages_from_response(response)
    #     if messages:
    #         return messages

    def get_context_data(self, **kwargs):
        context = {}
        # context["messages"] = self.retrieve_sqs_messages()
        context["dogs"] = Dog.objects.all()
        return context
