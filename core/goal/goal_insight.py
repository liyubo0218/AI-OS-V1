class GoalInsight:
    """
    AI-OS Goal Insight

    负责：
    - 分析目标状态
    - 生成目标洞察

    不负责：
    - 创建任务
    - 执行任务
    - 修改目标
    """

    def analyze(
        self,
        goal
    ):
        if goal.progress >= 100:
            state = "completed"
            suggestion = "目标已经完成"

        elif goal.progress > 0:
            state = "progressing"
            suggestion = "继续推进当前目标"

        else:
            state = "started"
            suggestion = "目标刚开始，需要制定推进计划"

        return {
            "goal": goal.name,
            "state": state,
            "progress": goal.progress,
            "status": goal.status,
            "suggestion": suggestion
        }

    def analyze_lifecycle(
        self,
        lifecycle
    ):
        """
        分析 GoalLifecycleMonitor 输出

        负责：
        - 解释生命周期状态

        不负责：
        - 修改目标
        - 创建任务
        - 执行任务
        """

        status = lifecycle.get(
            "status"
        )

        goal_name = lifecycle.get(
            "title",
            lifecycle.get(
                "goal_id"
            )
        )

        if status == "stalled":
            return {
                "goal": goal_name,
                "state": "stalled",
                "suggestion": lifecycle.get(
                    "suggestion",
                    "目标可能停滞"
                )
            }

        return {
            "goal": lifecycle.get(
                "title"
            ),
            "state": status,
            "suggestion": None
        }
