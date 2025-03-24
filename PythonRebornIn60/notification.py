# Exercise 5: Polymorphism with Notification Systems
# Objective: Send notifications through different channels using polymorphism.

# Instructions:
# Create a base class Notification with a method send(self, message) that raises a NotImplementedError.
# Create three derived classes:
# EmailNotification that overrides send(self, message) to print "Sending email: <message>"
# SMSNotification that overrides send(self, message) to print "Sending SMS: <message>"
# PushNotification that overrides send(self, message) to print "Sending push notification: <message>"
# Write a function notify(notification, message) that takes a Notification object and a message, then calls send(message).
# In main(), create a list of notifications (one of each type), and use a loop to call notify() with the message "Hello!" for each.


class Notification:
    def send(self, message):
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Sending push notification: {message}")


def notify(notification, message):
    notification.send(message)


def main():
    notifications = [EmailNotification(), SMSNotification(), PushNotification()]

    for notification in notifications:
        notify(notification, "Hello!")


if __name__ == "__main__":
    main()
