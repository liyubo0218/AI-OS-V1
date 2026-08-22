class MemoryPolicy:
    """
    AI-OS 记忆策略层

    负责：
    - 判断记忆价值
    - 分类记忆

    不负责：
    - AI推理
    - 任务执行
    """

    def __init__(self):
        self.rules = {
            "preference": 3,
            "profile": 3,
            "goal": 3,
            "task": 2,
            "temporary": 1
        }


    def classify(
        self,
        data
    ):
        text = str(data)

        if any(
            word in text
            for word in [
                "喜欢",
                "习惯",
                "偏好"
            ]
        ):
            return "preference"

        if any(
            word in text
            for word in [
                "目标",
                "计划"
            ]
        ):
            return "goal"

        return "temporary"


    def should_store(
        self,
        data
    ):
        category = self.classify(
            data
        )

        return (
            self.rules.get(
                category,
                0
            ) >= 2
        )


    def priority(
        self,
        data
    ):
        category = self.classify(
            data
        )

        return self.rules.get(
            category,
            0
        )
