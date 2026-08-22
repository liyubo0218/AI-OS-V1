class Orchestrator:
    """
    AI-OS 总协调器

    负责：
    - 连接核心模块
    - 编排请求流程
    - 返回统一结果

    不负责：
    - AI推理
    - 手机执行
    - 记忆学习
    """

    def __init__(
        self,
        secretary=None,
        brain=None,
        memory=None,
        task_manager=None,
        device=None
    ):
        self.secretary = secretary
        self.brain = brain
        self.memory = memory
        self.task_manager = task_manager
        self.device = device


    def process(
        self,
        user_input
    ):
        result = {
            "input": user_input
        }


        context = {}

        if self.memory:
            context = self.memory.get_memory_context(
                user_input
            )

        result["memory"] = context


        if self.secretary:
            result["secretary"] = (
                self.secretary.process(
                    user_input,
                    context
                )
            )


        if self.brain:
            result["brain"] = (
                self.brain.understand(
                    {
                        "user_input": user_input,
                        "memory": context
                    }
                )
            )


        if self.task_manager:
            task = self.task_manager.create_task(
                user_input
            )

            result["task"] = task.to_dict()


        return result
