from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="Heyy! Pragya here",
                     from_='+14342904181',
                     to='+919205201181'
                 )

print(message.sid)