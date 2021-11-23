from django.test import TestCase

import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(today)
print(yesterday)
print(tomorrow)