from .action_manager import ActionManager
from .tool_router import ToolRouter


class Executor:


    def __init__(self):

        self.actions = ActionManager()

        self.router = ToolRouter()


    def execute(
        self,
        action,
        payload=None
    ):

        return self.actions.execute(
            action,
            payload
        )


    def register_action(
        self,
        name,
        handler
    ):

        return self.actions.register(
            name,
            handler
        )
