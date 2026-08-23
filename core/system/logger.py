from datetime import datetime


class Logger:
    """
    AI-OS System Logger

    负责：
    - 记录系统日志
    - 提供日志查询

    不负责：
    - 日志存储
    - 日志分析
    """

    def __init__(
        self
    ):
        self.logs = []


    def write(
        self,
        message,
        level="INFO",
        module="system"
    ):
        self.logs.append(
            {
                "time":
                    datetime.utcnow().isoformat(),
                "level": level,
                "module": module,
                "message": message
            }
        )


    def get_logs(
        self
    ):
        return self.logs
