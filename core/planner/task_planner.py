class TaskPlanner:
    """
    AI-OS Task Planner V2.0

    负责：
    - 将用户确认后的建议转换为任务计划

    不负责：
    - 用户确认
    - 保存任务
    - 执行任务
    """

    def create_task_plan(
        self,
        confirmation,
        suggestion
    ):
        if not confirmation.get(
            "confirmed",
            False
        ):
            return {
                "status": "rejected",
                "task": None
            }

        return {
            "status": "ready",
            "task": {
                "title": suggestion,
                "description": "",
                "status": "pending"
            }
        }


    def commit_task(
        self,
        task_manager,
        confirmation,
        task_plan
    ):
        if not confirmation.get(
            "confirmed",
            False
        ):
            return {
                "status": "rejected",
                "task": None
            }

        if task_plan.get(
            "status"
        ) != "ready":
            return {
                "status": "invalid",
                "task": None
            }

        task_data = task_plan.get(
            "task",
            {}
        )

        task = task_manager.create_task(
            task_data.get(
                "title",
                ""
            ),
            task_data.get(
                "description",
                ""
            )
        )

        return {
            "status": "created",
            "task": task.to_dict()
        }
