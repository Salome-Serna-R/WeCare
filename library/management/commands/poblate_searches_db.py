from django.core.management.base import BaseCommand
from library.models import Searches
import os
from django.core.files import File
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the search table with initial data'

    def handle(self, *args, **kwargs):
        data = Searches(choice="Depression")
        data.save()
        data = Searches(choice="Depression")
        data.save()
        data = Searches(choice="Depression")
        data.save()
        data = Searches(choice="Depression")
        data.save()
        data = Searches(choice="Depression")
        data.save()
        data = Searches(choice="Depression")
        data.save()
        data = Searches(choice="Depression")
        data.save()
        data = Searches(choice="Anxiety")
        data.save()
        data = Searches(choice="Anxiety")
        data.save()
        data = Searches(choice="Anxiety")
        data.save()
        data = Searches(choice="Anxiety")
        data.save()
        data = Searches(choice="Anxiety")
        data.save()
        data = Searches(choice="Anxiety")
        data.save()
        data = Searches(choice="Stress")
        data.save()
        data = Searches(choice="Stress")
        data.save()
        data = Searches(choice="Stress")
        data.save()
        data = Searches(choice="Stress")
        data.save()
        data = Searches(choice="Stress")
        data.save()
        data = Searches(choice="Stress")
        data.save()
        data = Searches(choice="Stress")
        data.save()
        data = Searches(choice="Stress")
        data.save()
        data = Searches(choice="Stress")
        data.save()
        data = Searches(choice="Stress")
        data.save()

        print('Search table populated')
        
