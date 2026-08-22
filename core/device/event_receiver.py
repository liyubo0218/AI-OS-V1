class EventReceiver:
    """
    AI-OS 手机事件接收层

    负责：
    - 接收外部事件
    - 标准化事件格式

    不负责：
    - 手机监听
    - 权限管理
    - 系统控制
    """

    def __init__(
        self,
        source="mobile"
    ):
        self.source = source


    def receive(
        self,
        event_type,
        payload=None,
        source=None
    ):
        """
        接收手机事件
        """

        return {
            "type": event_type,
            "source": source or self.source,
            "payload": payload or {}
        }


    def receive_notification(
        self,
        content
    ):
        return self.receive(
            "notification",
            {
                "content": content
            }
        )


    def receive_siri_input(
        self,
        text
    ):
        return self.receive(
            "siri_input",
            {
                "text": text
            }
        )


    def receive_shortcut_result(
        self,
        result
    ):
        return self.receive(
            "shortcut_result",
            {
                "result": result
            }
        )
