class TaskTracker:


    def __init__(self):

        self.progress = {}



    def update(
        self,
        task_id,
        value
    ):

        self.progress[task_id] = value


        return {
            "status": "updated"
        }



    def get(
        self,
        task_id
    ):

        return self.progress.get(
            task_id,
            0
        )
