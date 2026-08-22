class ShortcutBridge:
    """
    AI-OS iOS快捷指令桥接层

    负责：
    - 生成Shortcut请求
    - 转换执行参数

    不负责：
    - 控制手机
    - 绕过权限
    """

    def __init__(
        self,
        platform="ios"
    ):
        self.platform = platform


    def run_shortcut(
        self,
        shortcut_name,
        params=None
    ):
        """
        创建快捷指令执行请求
        """

        return {
            "status": "ready",
            "platform": self.platform,
            "shortcut": shortcut_name,
            "params": params or {}
        }


    def create_request(
        self,
        action,
        data=None
    ):
        """
        创建统一手机动作请求
        """

        return {
            "action": action,
            "data": data or {},
            "target": "shortcut"
        }
