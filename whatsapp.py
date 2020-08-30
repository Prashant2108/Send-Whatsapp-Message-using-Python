import os
from twilio.rest import Client

client = Client()

from_whatsapp_number = 'whatsapp:+1XXXXXXXXXX'
to_whatsapp_number = 'whatsapp:' + os.environ['MY_PHONE_NUMBER']

client.messages.create(body='Hello World!',
                       from_=from_whatsapp_number, to=to_whatsapp_number)
