class SecretaryCore:
    """
    AI-OS 私人秘书中枢

    负责：
    - 接收用户需求
    - 调度 Brain 理解
    - 获取 Memory 上下文
    - 调用 LLM Gateway 思考
    - 返回秘书处理结果

    不负责：
    - 模型推理
    - 手机控制
    - 数据存储
    - 具体执行
    """

    def __init__(
        self,
        brain=None,
        memory=None,
        llm_gateway=None,
        task_manager=None
    ):
        self.brain = brain
        self.memory = memory
        self.llm_gateway = llm_gateway
        self.task_manager = task_manager

    def process(
        self,
        request
    ):
        user_input = request.get(
            "user_input",
            ""
        )

        result = {
            "status": "success",
            "intent": None,
            "response": None,
            "task": None
        }

        memory_context = {}

        if self.memory:
            memory_context = self.memory.get_memory_context(
                user_input
            )

        if self.brain:
            brain_result = self.brain.understand(
                {
                    "user_input": user_input,
                    "memory": memory_context
                }
            )

            result["intent"] = brain_result.get(
                "intent"
            )

        if self.llm_gateway:
            result["response"] = self.llm_gateway.generate(
                user_input
            )

        if self.task_manager:
            result["task"] = self.task_manager.create(
                user_input
            )

        return result
