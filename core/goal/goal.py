from datetime import datetime
import uuid


class Goal:
    """
    AI-OS Goal Model

    负责：
    - 描述长期目标
    - 保存目标状态

    不负责：
    - 任务执行
    - AI推理
    """

    def __init__(
        self,
        name,
        description="",
        deadline=None
    ):
        self.id = str(
            uuid.uuid4()
        )

        self.name = name
        self.description = description
        self.deadline = deadline

        self.status = "active"
        self.progress = 0

        self.created_at = (
            datetime.now()
            .isoformat()
        )

    def update_progress(
        self,
        progress
    ):
        self.progress = progress

        if progress >= 100:
            self.status = "completed"

        return True

    def to_dict(
        self
    ):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "deadline": self.deadline,
            "status": self.status,
            "progress": self.progress,
            "created_at": self.created_at
        }
