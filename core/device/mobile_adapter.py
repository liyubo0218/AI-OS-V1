from .device_interface import DeviceInterface


class MobileAdapter(DeviceInterface):
    """
    AI-OS 手机设备适配层

    负责：
    - 转换手机动作请求
    - 对接手机能力接口

    不负责：
    - 实际系统控制
    - 权限绕过
    """

    def __init__(
        self,
        device_name="mobile"
    ):
        super().__init__(
            device_name
        )


    def execute(
        self,
        action,
        params=None
    ):
        """
        将AI-OS动作转换为手机请求

        实际执行由：
        Siri / Shortcut / App Intent
        完成
        """

        return {
            "status": "ready",
            "device": self.device_name,
            "action": action,
            "params": params or {}
        }


    def send_message(
        self,
        contact,
        text
    ):
        return self.execute(
            "send_message",
            {
                "contact": contact,
                "text": text
            }
        )


    def open_app(
        self,
        app_name
    ):
        return self.execute(
            "open_app",
            {
                "app": app_name
            }
        )


    def run_shortcut(
        self,
        shortcut_name
    ):
        return self.execute(
            "run_shortcut",
            {
                "shortcut": shortcut_name
            }
        )
