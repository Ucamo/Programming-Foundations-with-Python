from twilio.rest import TwilioRestClient

account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    to="+526621000000", 
    from_="+1YOURTWILIOPHONENUMBER",
    body="TextOfTheMessage")

print(message.sid)
