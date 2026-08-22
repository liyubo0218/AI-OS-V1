from .execution_registry import ExecutionRegistry
from .execution_status import ExecutionStatus



class ExecutionManager:


    def __init__(self):

        self.registry = ExecutionRegistry()

        self.status = ExecutionStatus()



    def register_executor(
        self,
        name,
        executor
    ):

        return self.registry.register(
            name,
            executor
        )



    def execute(
        self,
        name,
        request=None
    ):


        executor = self.registry.get(
            name
        )


        if executor is None:

            return {
                "status": "not_found"
            }



        self.status.update(
            name,
            "executing"
        )


        return {

            "status": "executed",

            "executor": executor,

            "request": request

        }
