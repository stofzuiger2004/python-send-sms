# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("SK2855527e8c3bf62457bb90113dbf0906", "YN3kJeHJ2tWvmrMehUzfLFpJslER86dM")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+32468307742", 
                       from_="+12078433545", 
                       body="Hello from Python!")
