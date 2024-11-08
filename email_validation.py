'''import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email : ")

if re.search(email_condition,user_email):
    print('Entered Email is Valid')
else:
    print("Enter a valid one")'''

import re

# Function to check email validity
def validate_email(email):
    email_condition = "^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if re.match(email_condition, email):
        return True
    return False

# Welcome message
print("Welcome to the Email Validation System!")
print("Please make sure your email follows this format: username@example.com")

# Loop to keep asking for a valid email
while True:
    user_email = input("\nEnter your Email: ").strip()  # Remove unnecessary spaces around input

    # Check if the email is valid
    if validate_email(user_email):
        print(f"\nEntered Email '{user_email}' is Valid! 🎉")
        break  # Exit the loop if the email is valid
    else:
        print("\nOops! That doesn't seem like a valid email. Please try again.")
        print("Make sure your email contains an '@' and a valid domain (e.g., gmail.com, yahoo.com).")

# Optionally, you can add a feature to give more specific feedback
# for common mistakes:
def email_feedback(email):
    if not "@" in email:
        return "Missing '@'. Email should contain '@'."
    if not "." in email:
        return "Missing domain. Email should contain a '.' after '@'."
    if len(email.split('@')) != 2:
        return "Email should only have one '@'."
    return "Looks good!"

print("\n--- Final Check ---")
print(f"Final validation message: {email_feedback(user_email)}")
