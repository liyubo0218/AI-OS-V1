class AIOSException(Exception):
    """
    AI-OS 统一异常类型

    用于：
    - 系统级错误传递

    不负责：
    - 错误存储
    - 错误恢复
    """

    def __init__(
        self,
        code,
        message
    ):
        self.code = code
        self.message = message

        super().__init__(
            message
        )


class ErrorResponse:
    """
    AI-OS 统一错误返回格式
    """

    @staticmethod
    def create(
        code,
        message
    ):
        return {
            "status": "error",
            "code": code,
            "message": message
        }


    @staticmethod
    def from_exception(
        error
    ):
        if isinstance(
            error,
            AIOSException
        ):
            return {
                "status": "error",
                "code": error.code,
                "message": error.message
            }

        return {
            "status": "error",
            "code": "unknown_error",
            "message": str(error)
        }
