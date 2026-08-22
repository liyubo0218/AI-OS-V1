class ActionMapper:
    """
    AI-OS 手机动作映射层

    负责：
    - AI动作转换为手机动作
    - 标准化执行参数

    不负责：
    - 手机执行
    - 用户理解
    """

    def __init__(self):
        self.action_map = {
            "reminder": {
                "mobile_action": "create_reminder",
                "channel": "shortcut"
            },
            "notification": {
                "mobile_action": "send_notification",
                "channel": "notification"
            },
            "message": {
                "mobile_action": "send_message",
                "channel": "shortcut"
            },
            "open_app": {
                "mobile_action": "open_application",
                "channel": "shortcut"
            }
        }


    def map_action(
        self,
        action,
        data=None
    ):
        template = self.action_map.get(
            action
        )

        if not template:
            return {
                "mobile_action": action,
                "channel": "unknown",
                "payload": data or {}
            }


        return {
            "mobile_action": template["mobile_action"],
            "channel": template["channel"],
            "payload": data or {}
        }


    def supported_actions(
        self
    ):
        return list(
            self.action_map.keys()
        )


    def add_mapping(
        self,
        action,
        mobile_action,
        channel
    ):
        self.action_map[action] = {
            "mobile_action": mobile_action,
            "channel": channel
        }

        return True


    def can_handle(
        self,
        action
    ):
        return action in self.action_map
