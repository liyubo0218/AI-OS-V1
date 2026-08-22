class TaskMemory:


    def __init__(
        self,
        storage
    ):

        self.storage = storage


    def save_task(
        self,
        task_id,
        task
    ):

        return self.storage.save(
            f"task:{task_id}",
            task
        )


    def get_task(
        self,
        task_id
    ):

        return self.storage.get(
            f"task:{task_id}"
        )
