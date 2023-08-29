class MessageSender:
    def send_message(self, message):
        pass

class EmailSender(MessageSender):
    def send_message(self, message):
        print(f"Sending email: {message}")

class TextSender(MessageSender):
    def send_message(self, message):
        print(f"Sending text: {message}")

class Message:
    def __init__(self, sender):
        self.sender = sender

    def send(self, message):
        self.sender.send_message(message)

email_sender = EmailSender()
message = Message(email_sender)
message.send("Hello via email!")  # Output: Sending email: Hello via email!

text_sender = TextSender()
message = Message(text_sender)
message.send("Hi via text!")  # Output: Sending text: Hi via text!
