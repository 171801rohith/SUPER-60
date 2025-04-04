# Exercise 3: Real-World Challenge
# Task: Build a logging system that appends timestamped messages to 'app.log' based on user input until they type “exit.”

# Instructions:
# Use datetime for timestamps.
# Format each log entry as “YYYY-MM-DD HH:MM:SS - message.”
# Expected Behavior: Entering “Started app” adds a line like “2023-10-15 14:30:45 - Started app” to 'app.log'.

# Hint: Use a while loop and datetime.datetime.now().

from datetime import datetime

while True:
    user_message = input("Enter a message ('exit' to stop): ")

    try:
        with open("app.log", "a") as file:
            timestmp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestmp} - {user_message}.\n")
            print("Log saved.")
    except Exception as e:
        print(e)
    if user_message.lower() == "exit":
        break
