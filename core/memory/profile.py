class UserProfile:
    """
    AI-OS 用户私人画像

    负责：
    - 保存用户长期偏好
    - 保存用户习惯
    - 保存重要信息索引

    不负责：
    - 自动分析用户
    - 数据采集
    - AI推理
    """

    def __init__(
        self
    ):
        self.profile = {
            "preferences": {},
            "habits": {},
            "important_info": {}
        }


    def set_value(
        self,
        category,
        key,
        value
    ):
        if category not in self.profile:
            return False

        self.profile[category][key] = value

        return True


    def get_value(
        self,
        category,
        key,
        default=None
    ):
        if category not in self.profile:
            return default

        return self.profile[category].get(
            key,
            default
        )


    def remove_value(
        self,
        category,
        key
    ):
        if category not in self.profile:
            return False

        if key in self.profile[category]:
            del self.profile[category][key]
            return True

        return False


    def get_profile(
        self
    ):
        return self.profile
