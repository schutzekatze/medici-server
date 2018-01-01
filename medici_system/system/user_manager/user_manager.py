import logging
from django.contrib.auth.models import User
from ...models import MediciUser
import datetime
from decimal import Decimal

logger = logging.getLogger("User Manager")

def process_receipt_data(mediciuser, data):
    logger.info("Received data:\n" + data + "\nProcessing...")

    mediciuser.balance -= data['total']

    logger.info("Data processed successfully.")

def user_create(user_data):
    logger.info("Creating user <" + user_data.userame + ">...")

    User.objects.create_user(
                            username=user_data['username'],
                            password=user_data['password'],
                            email=user_data['email']
                            )

    logger.info("User <" + user_data.userame + "> created successfully.")

def user_update(mediciuser, user_data):
    logger.info("Updating user <" + user_data.userame + ">...")

    if 'username' in user_data:
        mediciuser.user.username = user_data['username']
    if 'password' in user_data:
        mediciuser.user.set_password(user_data['password'])
    if 'email' in user_data:
        mediciuser.user.email = user_data['email']
    if 'balance' in user_data:
        mediciuser.balance = Decimal(user_data['balance'])
    mediciuser.last_updated = datetime.datetime.now()

    mediciuser.user.save()

    logger.info("User <" + medici.user.username + "> updated successfully.")

def user_fetch(mediciuser, user_fields):
    logger.info("Fetching user <" + user_data.userame + ">...")

    data = {}

    if 'username' in user_fields:
        data['username'] = mediciuser.user.username
    if 'email' in user_fields:
        data['email'] = mediciuser.user.email
    if 'balance' in user_fields:
        data['balance'] = mediciuser.balance
    if 'last_updated' in user_fields:
        data['last_updated'] = mediciuser.last_updated

    logger.info("User <" + medici.user.username + "> fetched successfully.")

    return data
