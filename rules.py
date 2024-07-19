import random
from intents import Intents
from responses import Responses

class RuleBot:
    neg_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later","no")
    random_questions = (
        "Why are you here?",
        "Are there any other bots like you?",
        "Can you tell me about another existing chatbot?",
        "Does WhatsApp have a chatbot?",
        "What do you consume for sustenance?",
        "What chatbots have you used?",
        "Which chatbot is the best according to you?"
    )

    def __init__(self):
        self.name = ""
    
    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(f"Hi {self.name}, I am RuleBot. Will you help me learn about other existing chatbots?\n").lower()
        if will_help in self.neg_responses:
            print("No problem, take care and have a nice day ahead.")
        else:
            self.chat()
    
    def make_exit(self, reply):
        if reply in self.exit_commands:
            print("Okay, Enjoy your day!")
            return True
        return False
    
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            intent = Intents.match_intent(reply)
            if intent:
                response = Responses.get_response(intent)
            else:
                response = Responses.get_response('no_match_intent')
            reply = input(response + "\n").lower()

# Initialize and start the chatbot
if __name__ == "__main__":
    Alienbot = RuleBot()
    Alienbot.greet()
