from datetime import datetime


class GoalModel:
    """
    AI-OS Goal 目标对象

    负责：
    - 保存目标信息
    - 保存目标状态
    - 保存目标进度

    不负责：
    - 目标监控
    - 任务执行
    - AI推理
    """

    def __init__(
        self,
        goal,
        deadline=None
    ):
        self.goal = goal
        self.deadline = deadline
        self.status = "created"
        self.progress = 0
        self.created_at = datetime.utcnow()


    def update(
        self,
        status
    ):
        self.status = status


    def update_progress(
        self,
        progress
    ):
        self.progress = progress


    def to_dict(
        self
    ):
        return {
            "goal": self.goal,
            "deadline": self.deadline,
            "status": self.status,
            "progress": self.progress,
            "created_at":
                self.created_at.isoformat()
        }
