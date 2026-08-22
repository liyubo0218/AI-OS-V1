class TaskScheduler:


    def __init__(self):

        self.tasks = []



    def schedule(
        self,
        task
    ):

        self.tasks.append(
            task
        )


        return {
            "status": "scheduled"
        }



    def list_tasks(
        self
    ):

        return self.tasks
