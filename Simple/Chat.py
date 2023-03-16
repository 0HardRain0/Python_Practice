import random


def greet():
    greetings = ["Hi there!", "Hello!", "Hey!", "Greetings!"]
    return random.choice(greetings)

def get_response(user_input):
    responses = {
        "what's up?": "Not much, how about you?",
        "how are you?": "I'm doing well, thanks for asking.",
        "goodbye": "Goodbye, have a nice day!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what's your name?": "My name is ChatBot."
    }
    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return "I'm sorry, I didn't understand what you said."
    
    
print(greet())

while True:
    user_input = input("You: ")
    if user_input.lower()=="exit":
        print("ChatBot: Goodbye!")
        break
    else:
        print("ChatBot: " + get_response(user_input))