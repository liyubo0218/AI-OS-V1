class MemoryService:
    """
    AI-OS Memory 统一服务入口

    负责：
    - 统一访问用户记忆
    - 提供秘书上下文
    - 管理 Profile 接口

    不负责：
    - AI推理
    - 自动学习
    - 数据采集
    """

    def __init__(
        self,
        profile=None,
        user_memory=None,
        task_memory=None
    ):
        self.profile = profile
        self.user_memory = user_memory
        self.task_memory = task_memory


    def save_profile(
        self,
        category,
        key,
        value
    ):
        if not self.profile:
            return False

        return self.profile.set_value(
            category,
            key,
            value
        )


    def get_profile(
        self
    ):
        if not self.profile:
            return {}

        return self.profile.get_profile()


    def get_memory_context(
        self,
        query=""
    ):
        result = {
            "profile": self.get_profile(),
            "memory": {},
            "tasks": {}
        }

        if self.user_memory:
            result["memory"] = self.user_memory.search(
                query
            )

        if self.task_memory:
            result["tasks"] = self.task_memory.get_tasks()

        return result
