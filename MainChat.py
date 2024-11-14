
import time
import json
import random
from difflib import get_close_matches
from Weather import weatherapp

data_file = open('intents.json').read()
intents = json.loads(data_file)

def load_knowledge(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str])-> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge: dict) -> str | None:
    for q in knowledge["questions"]:
        if q["question"] == question:
            return q["answer"]


def chatbot():
    knowledge: dict = load_knowledge('knowledge.json')
    options = ['->Weather', '->Convo','->Advice', '->News']
    print('Hey There! I am your chatbot assistant!\nHere are some  options to help you get started')
    for option in options:
        print(option)

    while True:
        user_input = input('Main option input -->').lower()
        if user_input == "exit":
            exit()

        if 'weather' in user_input:
            print('collecting weather data.....')
            time.sleep(1)
            weatherapp()

        if 'convo' in user_input:
            print("(Say bye to exit too option page)")
            while True:
                user_input2 = input('Talk here:').lower()
                if user_input2 == "bye":
                    break

                response_found = False

                for intent in intents['intents']:
                    for pattern in intent['patterns']:
                        if user_input2 == pattern.lower():
                            chatbot_response = random.choice(intent['responses'])
                            print("Chatbot:", chatbot_response)
                            response_found = True
                            break

                    if response_found:
                        break

                if not response_found:
                    best_match: str | None = find_best_match(user_input,[q["question"] for q in knowledge["questions"]])

                    if best_match:
                        answer: str = get_answer_for_question(best_match, knowledge)
                        print(f'Chatbot: {answer}')
                    else:
                        print("sorry i didnt get that teach me")
                        new_answer: str = input('type the answer or "skip":')

                        if new_answer.lower() != 'skip':
                            knowledge["questions"].append({"question": user_input, "answer": new_answer})
                            save_knowledge('knowledge.json', knowledge)
                            print('thank you ive learnt a response')


chatbot()