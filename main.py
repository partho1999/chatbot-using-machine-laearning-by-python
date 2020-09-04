from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot("Jarvis")

conversation = [
    "Hello",
    "Hi there!",
    "what's your name",
    "i'm jarvis",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

while True:
    try:
        user_input = input('You: ')

        bot_response = chatbot.get_response(user_input)

        print('bot: ',bot_response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break