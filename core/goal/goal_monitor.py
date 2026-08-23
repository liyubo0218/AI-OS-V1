class GoalMonitor:
    """
    AI-OS Goal Monitor

    负责：
    - 检查目标状态
    - 输出目标分析

    不负责：
    - 创建任务
    - 执行任务
    - 修改目标
    """

    def __init__(
        self,
        goal_manager=None
    ):
        self.goal_manager = goal_manager


    def check_goal(
        self,
        goal
    ):
        if goal.progress >= 100:
            state = "completed"
            message = "目标已完成"

        elif goal.progress > 0:
            state = "progressing"
            message = "目标正在推进"

        else:
            state = "started"
            message = "目标刚开始"

        return {
            "goal": goal.name,
            "state": state,
            "progress": goal.progress,
            "status": goal.status,
            "message": message
        }


    def check_all(
        self
    ):
        if not self.goal_manager:
            return []

        results = []

        for goal in self.goal_manager.goals:
            results.append(
                self.check_goal(
                    goal
                )
            )

        return results
