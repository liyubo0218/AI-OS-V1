class NotificationBridge:
    """
    AI-OS 手机通知桥

    负责：
    - 接收通知数据
    - 转换通知格式

    不负责：
    - 监听手机
    - 获取权限
    - 绕过系统
    """

    def __init__(
        self,
        platform="ios"
    ):
        self.platform = platform


    def receive_notification(
        self,
        title,
        content,
        source="iphone"
    ):
        return {
            "type": "notification",
            "platform": self.platform,
            "source": source,
            "title": title,
            "content": content
        }


    def create_event(
        self,
        notification
    ):
        return {
            "event_type": "notification",
            "payload": notification
        }
