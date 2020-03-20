import sys
import os
from twilio.rest import Client 
from dotenv import load_dotenv
import msg_templates 
load_dotenv()

#setup
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token) 
sender=os.getenv('SANDBOX_SENDER_NUMBER')
receiver=os.getenv('SANDBOX_RECEIVER_NUMBER')


def send_msg(text,sender=sender,receiver=receiver):
	try:
		message = client.messages.create( 
								from_=sender,  
								body=text,      
								to=receiver)
	except:
		print('Error: could not send message to ', receiver)
		
def broadcast_msg(friends):
	for friend in friends:
		send_msg(sender,receiver,customText(friend))

send_msg(msg_templates.simple_notification)
