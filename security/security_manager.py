class SecurityManager:

    def check_permission(self, task):

        task_text = task.get(
            "task",
            ""
        )


        high_risk_keywords = [
            "删除全部文件",
            "清空数据",
            "关闭系统"
        ]


        for keyword in high_risk_keywords:

            if keyword in task_text:

                return {
                    "allowed": False,
                    "risk_level": "high",
                    "reason": "需要用户授权"
                }


        return {
            "allowed": True,
            "risk_level": "low",
            "reason": "permission granted"
        }


    def authorize(self, task):

        return {
            "authorized": True,
            "task": task
        }
