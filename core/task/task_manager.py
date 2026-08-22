from .task import Task
from core.event.event import Event


class TaskManager:
    """
    AI-OS 任务管理中心

    负责：
    - 创建任务
    - 保存任务
    - 查询任务
    - 更新任务状态

    不负责：
    - 任务执行
    - 手机控制
    - AI推理
    """

    def __init__(
        self,
        event_bus=None
    ):
        self.tasks = []
        self.event_bus = event_bus


    def create_task(
        self,
        title,
        description="",
        deadline=None
    ):
        task = Task(
            title,
            description,
            deadline
        )

        self.tasks.append(
            task
        )


        if self.event_bus:
            event = Event(
                "task.created",
                task.to_dict()
            )

            self.event_bus.publish(
                event
            )

        return task


    def get_tasks(
        self
    ):
        return self.tasks


    def get_task(
        self,
        index
    ):
        if index < 0:
            return None

        if index >= len(
            self.tasks
        ):
            return None

        return self.tasks[index]


    def update_task_status(
        self,
        index,
        status
    ):
        task = self.get_task(
            index
        )

        if not task:
            return False

        return task.update_status(
            status
        )
