from django.core.management.base import BaseCommand, CommandError
import requests


class Command(BaseCommand):
    help = 'Type the help text here'

    def handle(*args, url,**options):
        response = requests.request(method="GET",url=url)
        return response.status_code
