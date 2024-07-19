import random

class Responses:
    responses = {
        'describe_chatbot_intent': [
            "There are many other chatbots existing.",
            "Not only chatbots but there are many other bots that solve your queries."
        ],
        'answer_why_intent': [
            "I come in peace.",
            "I am here to get to know more about other chatbots.",
            "I heard you have a great taste in chatbots."
        ],
        'about_copilot': [
            "Copilot has superpowers beyond chat.",
            "It’s a generative AI model that learns from its interactions."
        ],
        'about_ai': [
            "AI stands for Artificial Intelligence.",
            "AI is the simulation of human intelligence in machines.",
            "There are many applications of AI, including chatbots like me."
        ],
        'about_nlp': [
            "NLP stands for Natural Language Processing.",
            "NLP is a field of AI that focuses on the interaction between computers and humans through natural language.",
            "NLP allows chatbots to understand and respond to human language."
        ],
        'about_self': [
            "I am a rule-based chatbot designed to help you learn about other chatbots.",
            "My main function is to interact with you and provide information based on predefined rules."
        ],
        'no_match_intent': [
            "Sorry, I didn't get it.",
            "Please tell me more.",
            "I see. Can you elaborate?",
            "How do you think I feel when you say that?",
            "Interesting. Can you tell me more?"
        ]
    }

    @staticmethod
    def get_response(intent):
        return random.choice(Responses.responses[intent])
