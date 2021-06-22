import twilio
#print(twilio.__version__)

from twilio.rest import Client
#from moduleName.folder import class name

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC29d60278e448390b0d9103a188d552b5'
auth_token = 'f0f01e5faf0d689d0ccee1bf3cadbb5f'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+660615905056", 
    from_="+19123485540",
    body="Natthawee_Hongto (6105003161)")

print(message.sid)