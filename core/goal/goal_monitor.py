class GoalMonitor:
    """
    AI-OS Goal 目标监控器

    负责：
    - 检查目标状态
    - 返回目标监控结果

    不负责：
    - 保存目标
    - 执行任务
    - AI推理
    """

    def __init__(
        self,
        goal_manager=None
    ):
        self.goal_manager = goal_manager


    def check_goal(
        self,
        goal_id
    ):
        if not self.goal_manager:
            return {
                "status": "failed",
                "error": "goal_manager_unavailable"
            }

        goal = self.goal_manager.get_goal(
            goal_id
        )

        if goal is None:
            return {
                "status": "failed",
                "error": "goal_not_found"
            }

        return {
            "status": "checked",
            "goal": goal.to_dict()
        }


    def check_all(
        self
    ):
        if not self.goal_manager:
            return []

        results = []

        for goal_id in self.goal_manager.get_goals():
            results.append(
                self.check_goal(goal_id)
            )

        return results
