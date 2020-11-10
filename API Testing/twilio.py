import random
import sys

from twilio.rest import Client

number = random.randint(1000,9999)
number = str(number)

print("Example: +441234567893")
sendto = input("Enter the number you want to send too: ")


account_sid = 'AC4644653ff04a6fd101982db4dd398250'
auth_token = '576a001bbf978664f1e7c278481063c7'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Your verification code: "+number,
    from_="+441408955050",
    to=sendto
)

#print(message.sid)

attempts = 0

while attempts < 3:
    code = input("Please enter the code that you received: ")
    if code == number:
        print("The code you entered is correct! You may continue")
        break
    else:
        attempts = attempts + 1
        attempts_left = 3 - attempts
        if attempts_left == 2:
            print("Code is incorrect, you have {} attempts left".format(attempts_left))
        elif attempts_left == 1:
            print("Code is incorrect, you have {} more attempt left".format(attempts_left))
        if attempts == 3:
            print("You have attempted too many times, Program will now terminate")
            sys.exit()
        else:
            pass
