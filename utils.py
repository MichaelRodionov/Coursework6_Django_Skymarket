import os
import time

import django
from skymarket.settings import BASE_DIR

# ----------------------------------------------------------------
# setup env settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skymarket.settings')
django.setup()


# ----------------------------------------------------------------
# run postgres container
time.sleep(2)
print(f'----------------------------------------------------------------\n'
      f'STARTING POSTGRES CONTAINER WITH DATABASE AND FRONTEND...\n'
      f'----------------------------------------------------------------')
time.sleep(2)
os.system(f'cd market_postgres && docker-compose up --build -d')


# ----------------------------------------------------------------
# migrations
time.sleep(2)
print('----------------------------------------------------------------\n'
      'MIGRATIONS...\n'
      '----------------------------------------------------------------')
time.sleep(2)
os.system(f'cd {BASE_DIR} && ./manage.py makemigrations')
os.system(f'cd {BASE_DIR} && ./manage.py migrate')


# ----------------------------------------------------------------
# load data to database
time.sleep(2)
print(f'----------------------------------------------------------------\n'
      f'LOADING DATA TO DATABASE...\n'
      f'----------------------------------------------------------------')
time.sleep(2)
os.system(f'cd {BASE_DIR} '
          f'&& ./manage.py loaddata fixtures/user.json'
          f'&& ./manage.py loaddata fixtures/ad.json'
          f'&& ./manage.py loaddata fixtures/comment.json'
          )


# ----------------------------------------------------------------
# run server
time.sleep(2)
print(f'----------------------------------------------------------------\n'
      f'RUNNING SERVER...\n'
      f'----------------------------------------------------------------')
time.sleep(2)
os.system(f'cd {BASE_DIR} && ./manage.py runserver')
