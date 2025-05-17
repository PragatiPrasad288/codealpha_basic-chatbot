import nltk
nltk.download('punkt')


import nltk
import random
import string


responses = {
    "greetings": ["Hello!", "Hi there!", "Hey!", "Howdy!", "Hi!"],
    "farewells": ["Goodbye!", "See you later!", "Bye!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "unknown": ["I'm not sure I understand.", "Can you rephrase that?", "Interesting... Tell me more."],
}

def classify_input(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greetings"
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "farewells"
    elif any(word in user_input for word in ["thanks", "thank you"]):
        return "thanks"
    else:
        return "unknown"


def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence)
    tokens = [word.lower() for word in tokens if word not in string.punctuation]
    return tokens

def chatbot():
    print(" ChatBot: Hello! I'm ChatBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print(" ChatBot:", random.choice(responses["farewells"]))
            break

        category = classify_input(user_input)
        reply = random.choice(responses[category])
        print(" ChatBot:", reply)

if __name__ == "__main__":
    chatbot()
