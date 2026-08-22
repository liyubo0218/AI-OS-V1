class TaskMonitor:
    """
    AI-OS 任务状态监督器

    负责：
    - 检查任务状态
    - 提供任务统计

    不负责：
    - 执行任务
    - 手机控制
    - AI推理
    """

    def __init__(
        self,
        task_manager
    ):
        self.task_manager = task_manager


    def get_pending_tasks(
        self
    ):
        tasks = self.task_manager.get_tasks()

        return [
            task
            for task in tasks
            if task.status == "pending"
        ]


    def get_running_tasks(
        self
    ):
        tasks = self.task_manager.get_tasks()

        return [
            task
            for task in tasks
            if task.status == "running"
        ]


    def status_report(
        self
    ):
        tasks = self.task_manager.get_tasks()

        result = {
            "total": len(tasks),
            "pending": 0,
            "running": 0,
            "completed": 0,
            "failed": 0
        }

        for task in tasks:
            if task.status in result:
                result[task.status] += 1

        return result
