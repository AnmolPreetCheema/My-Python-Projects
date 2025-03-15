import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you? "],
        "how are you": ["I'm just a bot, but I'm doing great! How about you?", "I'm fine! Thanks for asking!"],
        "what is your name": ["I'm Jimmy"],
        "bye": ["Goodbye! Have a great day! ", "See you later!"],
        "thanks": ["You're welcome!", "Glad I could help!"],
        "default": ["I'm not sure I understand. Can you ask something else?", "Hmm... I don't know that one."]
    }

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(responses["default"])

print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:bye")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")

