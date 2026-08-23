class ReasoningContext:
    """
    AI-OS Reasoning 上下文对象

    负责：
    - 组织推理输入

    不负责：
    - AI推理
    - 任务执行
    """

    def __init__(
        self,
        user_input,
        memory=None,
        task=None,
        goal=None
    ):
        self.user_input = user_input
        self.memory = memory or {}
        self.task = task or {}
        self.goal = goal or {}


    def to_dict(
        self
    ):
        return {
            "user_input": self.user_input,
            "memory": self.memory,
            "task": self.task,
            "goal": self.goal
        }
