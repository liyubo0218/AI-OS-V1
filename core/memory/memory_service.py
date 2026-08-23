from core.memory.memory_record import MemoryRecord


class MemoryService:
    """
    AI-OS Memory v2 统一服务入口

    负责：
    - 用户记忆访问
    - Profile管理
    - MemoryRecord管理
    - 上下文组合

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
        self.records = []


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


    def remember(
        self,
        memory_type,
        content,
        importance=0.5
    ):
        record = MemoryRecord(
            memory_type,
            content,
            importance
        )

        self.records.append(
            record
        )

        return record


    def recall(
        self,
        keyword=""
    ):
        results = []

        keyword = str(
            keyword
        )

        for record in self.records:

            content = str(
                record.content
            )

            # 完整匹配
            if keyword in content:
                results.append(
                    record.to_dict()
                )
                continue

            # 中文关键词匹配
            keywords = [
                "会议",
                "安排",
                "上午",
                "下午",
                "喜欢",
                "习惯",
                "偏好"
            ]

            for word in keywords:
                if word in keyword and word in content:
                    results.append(
                        record.to_dict()
                    )
                    break

        return results


    def search(
        self,
        keyword=""
    ):
        return self.recall(
            keyword
        )


    def retrieve(
        self
    ):
        return [
            record.to_dict()
            for record in self.records
        ]


    def get_context(
        self,
        query=""
    ):
        return {
            "profile": self.get_profile(),
            "records": self.recall(query),
            "tasks": self.task_memory.get_tasks()
            if self.task_memory
            else {}
        }


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
