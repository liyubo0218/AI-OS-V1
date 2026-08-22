from datetime import datetime


class TaskScheduler:
    """
    AI-OS 任务调度层

    负责：
    - 任务时间管理
    - 到期检查
    - 状态维护

    不负责：
    - 任务执行
    - AI推理
    """

    def __init__(self):
        self.tasks = []


    def schedule(
        self,
        task
    ):
        item = {
            "id": len(self.tasks) + 1,
            "task": task,
            "status": "pending",
            "created": datetime.now().isoformat()
        }

        self.tasks.append(
            item
        )

        return item


    def get_tasks(
        self
    ):
        return self.tasks


    def check_due(
        self
    ):
        due_tasks = []

        now = datetime.now()

        for item in self.tasks:

            if item["status"] != "pending":
                continue

            task_time = item.get(
                "execute_time"
            )

            if not task_time:
                continue

            try:
                execute_time = datetime.fromisoformat(
                    task_time
                )

                if execute_time <= now:
                    due_tasks.append(
                        item
                    )

            except Exception:
                continue

        return due_tasks


    def complete(
        self,
        task_id
    ):
        for item in self.tasks:

            if item["id"] == task_id:
                item["status"] = "completed"
                return True

        return False


    def cancel(
        self,
        task_id
    ):
        for item in self.tasks:

            if item["id"] == task_id:
                item["status"] = "cancelled"
                return True

        return False


    def pending(
        self
    ):
        return [
            task
            for task in self.tasks
            if task["status"] == "pending"
        ]
