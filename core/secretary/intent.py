class IntentAnalyzer:
    """
    AI-OS 秘书意图识别层

    负责：
    - 用户目标分类
    - 基础实体提取

    不负责：
    - 推理
    - 执行
    """

    def __init__(self):
        self.rules = {
            "create_task": [
                "提醒",
                "安排",
                "计划",
                "预约"
            ],
            "query": [
                "查询",
                "查一下",
                "告诉我"
            ],
            "summarize": [
                "总结",
                "整理",
                "汇总"
            ],
            "execute": [
                "打开",
                "发送",
                "执行"
            ]
        }


    def detect_intent(
        self,
        text
    ):
        for intent, words in self.rules.items():

            for word in words:

                if word in text:
                    return intent

        return "unknown"


    def extract_entities(
        self,
        text
    ):
        entities = []

        keywords = [
            "明天",
            "今天",
            "上午",
            "下午",
            "晚上",
            "电话",
            "消息",
            "提醒"
        ]

        for item in keywords:

            if item in text:
                entities.append(
                    item
                )

        return entities


    def analyze(
        self,
        user_input
    ):
        intent = self.detect_intent(
            user_input
        )

        entities = self.extract_entities(
            user_input
        )

        confidence = 0.5

        if intent != "unknown":
            confidence = 0.8


        return {
            "intent": intent,
            "confidence": confidence,
            "entities": entities,
            "input": user_input
        }


    def supported_intents(
        self
    ):
        return list(
            self.rules.keys()
        )
