from .reasoning_context import ReasoningContext
from .reasoning_result import ReasoningResult


class ReasoningGateway:
    """
    AI-OS Reasoning Gateway

    负责：
    - 接收推理上下文
    - 生成标准推理结果

    不负责：
    - LLM实现
    - 任务执行
    - 设备控制
    """

    def __init__(
        self
    ):
        pass


    def reason(
        self,
        context
    ):
        if isinstance(
            context,
            ReasoningContext
        ):
            data = context.to_dict()
        else:
            data = context

        intent = "unknown"

        user_input = data.get(
            "user_input",
            ""
        )

        if "提醒" in user_input:
            intent = "create_task"

        return ReasoningResult(
            intent,
            {
                "context": data
            },
            0.5
        ).to_dict()
