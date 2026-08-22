class RuntimeManager:

    def __init__(self):
        self.tasks = {}


    def create_task(
        self,
        task_id,
        source,
        goal
    ):
        self.tasks[task_id] = {
            "task_id": task_id,
            "source": source,
            "goal": goal,
            "state": "created",
            "context": {},
            "result": None
        }

        return {
            "status": "created",
            "task_id": task_id
        }


    def update_state(
        self,
        task_id,
        state
    ):
        if task_id not in self.tasks:
            return {
                "status": "failed"
            }

        self.tasks[task_id]["state"] = state

        return {
            "status": "updated",
            "current_state": state
        }


    def update_context(
        self,
        task_id,
        context
    ):
        if task_id not in self.tasks:
            return {
                "status": "failed"
            }

        self.tasks[task_id]["context"] = context

        return {
            "status": "updated"
        }


    def record_result(
        self,
        task_id,
        result
    ):
        if task_id not in self.tasks:
            return {
                "status": "failed"
            }

        self.tasks[task_id]["result"] = result

        return {
            "status": "recorded"
        }


    def get_task(
        self,
        task_id
    ):
        return self.tasks.get(
            task_id
        )
