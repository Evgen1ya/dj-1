import csv

from django.core.management.base import BaseCommand
from db.phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                item = Phone(id=phone[0], name=phone[1], image=phone[2], price=phone[3], release_date=phone[4], lte_exists=phone[5])
                item.save()

