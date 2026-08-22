class ActionManager:


    def __init__(self):

        self.actions = {}


    def register(
        self,
        name,
        handler
    ):

        self.actions[name] = handler

        return {
            "status": "registered"
        }


    def execute(
        self,
        name,
        payload=None
    ):

        if name not in self.actions:

            return {
                "status": "failed",
                "error": "action_not_found"
            }


        return self.actions[name](
            payload
        )
