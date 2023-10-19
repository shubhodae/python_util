from abc import ABC, abstractmethod
from dataclasses import dataclass


class Notification(ABC):
    @abstractmethod
    def nofity(self, message: str) -> None:
        pass


class Email(Notification):
    def __init__(self, email) -> None:
        self.email = email

    def nofity(self, message: str) -> None:
        print(f"Email with message: {message} send to email: {self.email}")


class SMS(Notification):
    def __init__(self, phone_number) -> None:
        self.phone_number = phone_number

    def nofity(self, message: str) -> None:
        print(
            f"SMS with message: {message} is send to phone_number {self.phone_number}"
        )


@dataclass
class Contact:
    name: str
    email: str
    phone_number: str


class NotificationManager:
    def __init__(self, notification: Notification) -> None:
        self.notificaiton = notification

    def send_notification(self, message):
        self.notificaiton.nofity(message)


if __name__ == "__main__":
    contact = Contact(name="John", email="john.doe@gmail.com", phone_number="987654321")

    sms_notification = SMS(contact.phone_number)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send_notification("Hello John to sms")

    notification_manager = NotificationManager(email_notification)
    notification_manager.send_notification("Hello Jhn to emal")
