class GoalLifecycleMonitor:
    """
    AI-OS Goal Lifecycle Monitor V2.5

    负责：
    - 记录目标生命周期
    - 更新目标状态
    - 检测目标停滞

    不负责：
    - 修改用户目标
    - 创建任务
    - 执行任务
    """

    def __init__(self):
        self.goals = []


    def create_goal_record(
        self,
        goal_id,
        title,
        status="created"
    ):
        record = {
            "goal_id": goal_id,
            "title": title,
            "status": status,
            "updates": 0
        }

        self.goals.append(
            record
        )

        return record


    def update_goal_status(
        self,
        goal_id,
        status
    ):
        for goal in self.goals:
            if goal["goal_id"] == goal_id:
                goal["status"] = status
                goal["updates"] += 1
                return goal

        return None


    def check_stagnation(
        self,
        goal_id
    ):
        for goal in self.goals:
            if goal["goal_id"] == goal_id:

                if goal["updates"] == 0:
                    return {
                        "goal_id": goal_id,
                        "status": "stalled",
                        "suggestion": "目标可能停滞，是否安排下一阶段任务？"
                    }

                return {
                    "goal_id": goal_id,
                    "status": goal["status"],
                    "suggestion": None
                }

        return None


    def get_goal_status(
        self,
        goal_id
    ):
        for goal in self.goals:
            if goal["goal_id"] == goal_id:
                return goal

        return None


    def get_goals(
        self
    ):
        return self.goals
