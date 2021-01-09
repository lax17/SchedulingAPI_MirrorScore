from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .constants import *
from .serializers import ScheduleApiSerializer
import platform
import socket
import subprocess
import requests
from datetime import datetime
from .management.commands import tasks
# Create your views here.




def api_call(url):
    return requests.request(method="GET",url=url)



class scheduleapi(APIView):
    def post(self,request):
        request_data = request.data
        serializer = ScheduleApiSerializer(data=request.data)
        if not serializer.is_valid():
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        # Sending A GET request to the Url
        response = api_call(url=request_data["url"])
        # when a current datetime matches parameter datetime task is invoked
        if datetime.now() == request_data["date_time"]:
            return Response(tasks.Command.handle(url=request_data["url"]))


class ping(APIView):
    def get(self,request):
        if request.query_params.get("host"):
            host = request.query_params.get("host")
        else:
            return Response(PARAMETER_MISSING,status=status.HTTP_400_BAD_REQUEST)
        try:
            ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
            args = "ping " + " " + ping_str + " " + host
            need_sh = False if platform.system().lower() == "windows" else True
            # Ping
            if subprocess.call(args, shell=need_sh) == 0 :
                return Response(SUCCESS_RESPONSE,status=status.HTTP_200_OK)
            else:
                return Response(FAILURE_RESPONSE,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(EXCEPTION_RESPONSE,status=status.HTTP_500_INTERNAL_SERVER_ERROR)







