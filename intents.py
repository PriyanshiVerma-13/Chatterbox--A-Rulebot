import re

class Intents:
    patterns = {
        'describe_chatbot_intent': r'.*\s*your bot.*',
        'answer_why_intent': r'why\sare.*',
        'about_copilot': r'.*\s*copilot.*',
        'about_ai': r'.*\s*ai.*',
        'about_nlp': r'.*\s*nlp.*',
        'about_self': r'.*\s*you.*'
    }

    @staticmethod
    def match_intent(reply):
        for intent, pattern in Intents.patterns.items():
            if re.match(pattern, reply):
                return intent
        return None
