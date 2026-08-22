class ExecutionStatus:


    def __init__(self):

        self.status = {}



    def update(
        self,
        task,
        value
    ):

        self.status[task] = value


        return {
            "status": "updated"
        }



    def get(
        self,
        task
    ):

        return self.status.get(
            task,
            "unknown"
        )
