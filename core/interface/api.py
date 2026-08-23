class AIOSAPI:
    """
    AI-OS 外部调用接口

    负责：
    - 接收外部请求
    - 调用Runtime

    不负责：
    - AI推理
    - 任务执行
    - 手机控制
    """

    def __init__(
        self,
        runtime=None
    ):
        self.runtime = runtime


    def handle_request(
        self,
        request
    ):
        if not self.runtime:
            from core.system.error import ErrorResponse

            return ErrorResponse.create(
                "runtime_unavailable",
                "runtime unavailable"
            )

        user_input = request.get(
            "user_input",
            ""
        )

        result = self.runtime.handle(
            user_input
        )

        return {
            "status": "success",
            "result": result
        }


    def health_check(
        self
    ):
        return {
            "status": "ok"
        }
