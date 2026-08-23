class MobileResult:
    """
    AI-OS Mobile 执行结果

    负责：
    - 统一执行返回格式

    不负责：
    - 执行动作
    - 设备管理
    """

    def __init__(
        self,
        status,
        action,
        data=None
    ):
        self.status = status
        self.action = action
        self.data = data or {}


    def to_dict(
        self
    ):
        return {
            "status": self.status,
            "action": self.action,
            "data": self.data
        }
