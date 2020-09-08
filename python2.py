# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("AC8f15d0443944ede040ce58edf3ebdc4d", "3dcdfe2e3898389ac16df10e4de3dafe")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+32468307742", 
                       from_="+12078433545", 
                       body="Hello from Python! Twilio trial account")
