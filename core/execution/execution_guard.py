class ExecutionGuard:
    """
    AI-OS Execution Guard V2.2

    负责：
    - 创建执行请求
    - 管理执行授权状态

    不负责：
    - 执行任务
    - 控制设备
    - 修改任务
    """

    def __init__(self):
        self.requests = []


    def request_execution(
        self,
        task
    ):
        request = {
            "task": task,
            "status": "pending",
            "approved": False
        }

        self.requests.append(
            request
        )

        return request


    def approve_execution(
        self,
        request
    ):
        request["status"] = "approved"
        request["approved"] = True

        return request


    def get_requests(
        self
    ):
        return self.requests
