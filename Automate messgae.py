'''import pywhatkit as pyw

pyw.sendwhatmsg('+919820529712','Hello Mohammed Amin here',10,43)'''

import pywhatkit as pyw
import datetime

# Get the current time
now = datetime.datetime.now()

# Calculate the time 2 minutes ahead
hour = now.hour
minute = now.minute + 2  # Adding 2 minutes to the current time

# If the minute exceeds 59, reset minute to 0 and increase the hour
if minute >= 60:
    minute -= 60  # Set minute to 0 and increment hour
    hour += 1

# Format the phone number (include country code)
phone_no = '+919820529712'

# The message to be sent
message = 'Hello Mohammed Amin here'

# Send the message at the calculated time
pyw.sendwhatmsg(phone_no, message, hour, minute)

# Print the time when the message will be sent
print(f"Message will be sent at {hour:02d}:{minute:02d}!")

