class ExecutionRegistry:


    def __init__(self):

        self.executors = {}



    def register(
        self,
        name,
        executor
    ):

        self.executors[name] = executor


        return {
            "status": "registered"
        }



    def get(
        self,
        name
    ):

        return self.executors.get(
            name
        )
