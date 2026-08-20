class Planner:

    def create_plan(self, understanding):

        intent = understanding.get(
            "intent",
            "unknown"
        )

        goal = understanding.get(
            "goal",
            ""
        )

        plan = {
            "task_id": "task_001",
            "goal": goal,
            "steps": [],
            "status": "ready"
        }


        if intent == "test_system":

            plan["steps"] = [
                "分析任务",
                "执行测试",
                "返回结果"
            ]

        elif intent == "file_task":

            plan["steps"] = [
                "查找文件",
                "分析文件",
                "整理文件"
            ]

        else:

            plan["steps"] = [
                "分析目标",
                "生成执行方案"
            ]


        return plan
