class TaskRuntime:

    def __init__(self):
        self.tasks = {}


    def create_task(
        self,
        goal
    ):
        task = {
            "task_id": "task_001",
            "goal": goal,
            "status": "created",
            "result": None
        }

        self.tasks["task_001"] = task

        return task


    def update_status(
        self,
        task_id,
        status,
        result=None
    ):
        task = self.tasks[task_id]

        task["status"] = status
        task["result"] = result

        return task


    def get_task(
        self,
        task_id
    ):
        return self.tasks.get(task_id)
