class DeviceInterface:
    """
    AI-OS Device Body 抽象接口

    负责：
    - 定义手机能力调用格式
    - 统一设备返回结构

    不负责：
    - 实际控制手机
    - 绕过系统权限
    """

    def __init__(
        self,
        device_name="unknown"
    ):
        self.device_name = device_name


    def execute(
        self,
        action,
        params=None
    ):
        """
        执行设备请求

        子类实现真实设备调用
        """

        return {
            "status": "unsupported",
            "device": self.device_name,
            "action": action,
            "params": params or {}
        }


    def get_capabilities(
        self
    ):
        """
        返回设备能力列表
        """

        return [
            "send_message",
            "open_app",
            "read_notification",
            "run_shortcut"
        ]
