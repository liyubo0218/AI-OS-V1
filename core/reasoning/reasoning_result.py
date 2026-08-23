class ReasoningResult:
    """
    AI-OS Reasoning 输出结果

    负责：
    - 标准化推理结果

    不负责：
    - 执行动作
    """

    def __init__(
        self,
        intent,
        plan=None,
        confidence=0.0
    ):
        self.intent = intent
        self.plan = plan or {}
        self.confidence = confidence


    def to_dict(
        self
    ):
        return {
            "intent": self.intent,
            "plan": self.plan,
            "confidence": self.confidence
        }
