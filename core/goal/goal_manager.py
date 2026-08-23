from .goal import Goal


class GoalManager:
    """
    AI-OS Goal Manager

    负责：
    - 创建目标
    - 保存目标
    - 查询目标
    - 更新目标

    不负责：
    - 任务执行
    - 自动规划
    """

    def __init__(
        self
    ):
        self.goals = []

    def create_goal(
        self,
        name,
        description="",
        deadline=None
    ):
        goal = Goal(
            name,
            description,
            deadline
        )

        self.goals.append(
            goal
        )

        return goal

    def get_goals(
        self
    ):
        return [
            goal.to_dict()
            for goal in self.goals
        ]

    def get_goal(
        self,
        goal_id
    ):
        for goal in self.goals:
            if goal.id == goal_id:
                return goal

        return None

    def update_progress(
        self,
        goal_id,
        progress
    ):
        goal = self.get_goal(
            goal_id
        )

        if not goal:
            return False

        return goal.update_progress(
            progress
        )
