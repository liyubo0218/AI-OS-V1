class ContextBuilder:
    """
    AI-OS Brain 上下文构建器

    负责：
    - 汇总用户输入
    - 融合记忆
    - 融合任务状态
    - 生成LLM上下文

    不负责：
    - AI推理
    - 任务执行
    """

    def __init__(
        self,
        memory_service=None
    ):
        self.memory_service = memory_service


    def _get_memory(
        self,
        query
    ):
        if not self.memory_service:
            return {}

        if hasattr(
            self.memory_service,
            "search"
        ):
            return self.memory_service.search(
                query
            )

        return {}


    def build(
        self,
        user_input,
        memory=None,
        task=None,
        state=None
    ):
        context = {
            "user_input": user_input,
            "memory": {},
            "task": task or {},
            "state": state or {}
        }

        if memory:
            context["memory"] = memory
        else:
            context["memory"] = self._get_memory(
                user_input
            )

        return context


    def build_prompt_context(
        self,
        context
    ):
        return {
            "role": "assistant_secretary",
            "context": context
        }


    def merge(
        self,
        base,
        extra
    ):
        result = {}

        if base:
            result.update(
                base
            )

        if extra:
            result.update(
                extra
            )

        return result
