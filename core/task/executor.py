class TaskExecutor:
    """
    AI-OS 任务执行层

    负责：
    - 执行任务
    - 调用设备能力
    - 返回结果

    不负责：
    - 意图分析
    - 任务规划
    """

    def __init__(
        self,
        device=None
    ):
        self.device = device
        self.history = []


    def execute(
        self,
        task
    ):
        action = task.get(
            "action",
            "unknown"
        )

        result = {
            "status": "failed",
            "action": action
        }


        if self.device:

            try:
                response = self.device.execute(
                    action,
                    task
                )

                result = {
                    "status": "success",
                    "action": action,
                    "result": response
                }

            except Exception as error:

                result = {
                    "status": "error",
                    "message": str(error)
                }


        else:

            result = {
                "status": "success",
                "action": action,
                "mode": "simulation"
            }


        self.history.append(
            {
                "task": task,
                "result": result
            }
        )


        return result


    def execute_batch(
        self,
        tasks
    ):
        results = []

        for task in tasks:

            results.append(
                self.execute(
                    task
                )
            )

        return results


    def get_history(
        self
    ):
        return self.history


    def clear_history(
        self
    ):
        self.history = []

        return True
