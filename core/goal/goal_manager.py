import uuid

from .goal_model import GoalModel


class GoalManager:
    """
    AI-OS Goal 管理中心

    负责：
    - 创建目标
    - 保存目标
    - 查询目标
    - 更新目标

    不负责：
    - 目标监控
    - 任务执行
    - AI推理
    """

    def __init__(
        self
    ):
        self.goals = {}


    def create_goal(
        self,
        title,
        deadline=None
    ):
        goal_id = str(
            uuid.uuid4()
        )

        goal = GoalModel(
            title,
            deadline
        )

        self.goals[goal_id] = goal

        return goal


    def get_goal(
        self,
        goal_id
    ):
        return self.goals.get(
            goal_id
        )


    def get_goals(
        self
    ):
        return self.goals


    def update_goal(
        self,
        goal_id,
        status
    ):
        goal = self.get_goal(
            goal_id
        )

        if goal is None:
            return False

        goal.update(
            status
        )

        return True
