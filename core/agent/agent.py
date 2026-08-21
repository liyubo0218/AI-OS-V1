class Agent:

    def __init__(self):
        self.tasks = {}


    def create_task(
        self,
        task
    ):

        if not task:
            return {
                "status": "failed",
                "reason": "invalid_task"
            }


        task_id = (
            f"task_{len(self.tasks)+1:03d}"
        )


        new_task = {
            "task_id": task_id,
            "action": task.get(
                "action",
                ""
            ),
            "parameters": task.get(
                "parameters",
                {}
            ),
            "status": "created",
            "result": None
        }


        self.tasks[task_id] = new_task

        return {
            "task_id": task_id,
            "status": "created"
        }


    def execute_task(
        self,
        task_id
    ):

        task = self.tasks.get(
            task_id
        )

        if not task:
            return {
                "status": "not_found"
            }


        task["status"] = "completed"

        task["result"] = (
            f"Executed: {task['action']}"
        )


        return {
            "task_id": task_id,
            "status": "completed",
            "result": task["result"]
        }


    def get_task_status(
        self,
        task_id
    ):

        task = self.tasks.get(
            task_id
        )

        if not task:
            return {
                "status": "not_found"
            }


        return {
            "task_id": task_id,
            "status": task["status"]
        }


    def get_result(
        self,
        task_id
    ):

        task = self.tasks.get(
            task_id
        )

        if not task:
            return {
                "status": "not_found"
            }


        return {
            "task_id": task_id,
            "status": task["status"],
            "result": task["result"]
        }
