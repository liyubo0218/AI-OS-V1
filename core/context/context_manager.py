class ContextManager:

    def __init__(self):
        self.context = {}

    def create_context(self, user_input):
        self.context = {
            "session_id": "session_001",
            "user_input": user_input,
            "goal": "",
            "task_state": "created",
            "metadata": {}
        }

        return self.context

    def get_context(self):
        return self.context

    def update_context(self, data):
        self.context.update(data)
        return self.context

    def clear_context(self):
        self.context = {}
        return True
