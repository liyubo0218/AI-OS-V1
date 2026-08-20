class ExecutionEngine:

    def execute(self, plan):

        task_id = plan.get(
            "task_id",
            "unknown"
        )

        steps = plan.get(
            "steps",
            []
        )

        result = {
            "task_id": task_id,
            "status": "running",
            "completed_steps": [],
            "result": ""
        }


        for step in steps:
            print("Running:", step)

            result["completed_steps"].append(
                step
            )


        result["status"] = "completed"

        result["result"] = "任务完成"

        return result
