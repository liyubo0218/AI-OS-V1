class BrainIntelligence:

    def __init__(self):
        pass


    def analyze(
        self,
        user_input,
        memory_context=None,
        goal_context=None
    ):
        return {
            "intent": self._detect_intent(user_input),
            "goal": user_input,
            "context": {
                "memory": memory_context,
                "goal": goal_context
            },
            "recommendation": "send_to_planner"
        }


    def _detect_intent(self, text):

        if not text:
            return "unknown"

        return "general_task"
