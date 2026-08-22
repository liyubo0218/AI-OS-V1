class Task:
    """
    AI-OS 任务基础对象

    负责：
    - 描述一个任务
    - 保存任务状态

    不负责：
    - 任务执行
    - 手机控制
    - AI推理
    """

    def __init__(
        self,
        title,
        description="",
        deadline=None
    ):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = "pending"


    def update_status(
        self,
        status
    ):
        allowed = [
            "pending",
            "running",
            "completed",
            "failed"
        ]

        if status not in allowed:
            return False

        self.status = status

        return True


    def to_dict(
        self
    ):
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "status": self.status
        }
