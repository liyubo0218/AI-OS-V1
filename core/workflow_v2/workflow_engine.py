from .workflow_state import WorkflowState
from .condition_handler import ConditionHandler
from .retry_manager import RetryManager



class WorkflowEngine:


    def __init__(self):

        self.state = WorkflowState()

        self.condition = ConditionHandler()

        self.retry = RetryManager()



    def create_workflow(
        self,
        steps
    ):

        self.steps = steps

        self.state.update(
            "ready"
        )


        return {
            "status": "created",
            "steps": steps
        }



    def run(
        self
    ):


        if not hasattr(
            self,
            "steps"
        ):

            return {
                "status": "failed"
            }


        self.state.update(
            "running"
        )


        self.state.update(
            "completed"
        )


        return {

            "status": "completed",

            "state": self.state.get()

        }
