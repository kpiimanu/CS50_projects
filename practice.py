# A list of short text messages
text_messages = ['Hi', 'BRB', 'WTF', 'LOL']

sent_messages = []

# Function to print each message
def show_message(text_msg):
    for text_msg in text_messages:
        print(text_msg)

# Function for moving each text msg from text_messages list to sent messages list
def send_messages(text_messages, sent_messages):
    while text_messages:
        text = text_messages.pop()
        sent_messages.append(text)

# Pass the list to the show message function to print each message
show_message(text_messages)
send_messages(text_messages, sent_messages)
print(f"\ntext_messages: {text_messages} ")
print('')
print(f"\nsent_messages: {sent_messages} ")