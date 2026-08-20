class TaskRuntime:


    def __init__(
        self,
        task_id
    ):

        self.task_id = task_id

        self.status = "created"



    def start(self):

        self.status = "running"


        return {
            "task_id": self.task_id,
            "status": self.status
        }



    def complete(self):

        self.status = "completed"


        return {
            "task_id": self.task_id,
            "status": self.status
        }
