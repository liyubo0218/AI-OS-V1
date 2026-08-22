from .intent_rules import match_intent


class IntentEngine:


    def analyze(
        self,
        text
    ):

        intent = match_intent(text)


        return {

            "intent": intent,

            "input": text

        }
