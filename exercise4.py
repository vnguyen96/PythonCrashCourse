#8-9 Messages

text_messages = ['where are you?', 'its late', 'time to go home']

def show_messages(messages):
    for message in messages:
        print(message)

show_messages(text_messages)
print("\n")

#8-10
text_messages = ['what time we do lunch?', 'cant do dinner', 'maybe 4']
sent_messages = []

def send_messages(messages, sent_messages):
        print("The following are unsent messages:")

        while messages:
            unsent_messages = messages.pop()
            print(unsent_messages)

            sent_messages.append(unsent_messages)

def show_sent_messages(sent_messages):
    print(f"\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)

send_messages(text_messages[:], sent_messages)
show_sent_messages(sent_messages)
