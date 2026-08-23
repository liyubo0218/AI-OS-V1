class ConfirmationManager:
    """
    AI-OS Confirmation Manager V1.9

    负责：
    - 创建确认请求
    - 保存确认状态
    - 返回用户确认结果

    不负责：
    - 创建任务
    - 执行任务
    - 自动批准
    """

    def __init__(self):
        self.requests = []


    def request_confirmation(
        self,
        message
    ):
        request = {
            "message": message,
            "status": "pending",
            "confirmed": False
        }

        self.requests.append(
            request
        )

        return request


    def confirm(
        self,
        request
    ):
        request["status"] = "confirmed"
        request["confirmed"] = True

        return request


    def get_requests(
        self
    ):
        return self.requests
