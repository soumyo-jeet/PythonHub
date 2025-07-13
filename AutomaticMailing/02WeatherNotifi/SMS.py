from twilio.rest import Client
import os
from dotenv import load_dotenv

acc_sid = os.getenv('TWILIO_ACCOUNT_SID')
acc_token = ""

client = Client(acc_sid, acc_token)
msg = client.messages.create(body="Hello messegeing from Twilio...Good Night!", from_="+19046010428", to="*************")

print(msg.status)
# WD7HCYHWCVV87KWZS12LZTBD