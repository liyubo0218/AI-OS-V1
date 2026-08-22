class SecretaryPlanner:
    """
    AI-OS 秘书规划层

    负责：
    - 根据意图生成执行计划
    - 协调模块调用顺序

    不负责：
    - 具体执行
    - AI推理
    """

    def __init__(self):
        self.routes = {
            "create_task": [
                "memory",
                "task",
                "device"
            ],
            "query": [
                "memory",
                "brain"
            ],
            "summarize": [
                "memory",
                "brain"
            ],
            "execute": [
                "device"
            ]
        }


    def get_modules(
        self,
        intent
    ):
        return self.routes.get(
            intent,
            [
                "brain"
            ]
        )


    def build_steps(
        self,
        modules
    ):
        steps = []

        for index, module in enumerate(
            modules
        ):

            steps.append(
                {
                    "step": index + 1,
                    "module": module
                }
            )

        return steps


    def plan(
        self,
        intent_result
    ):
        intent = intent_result.get(
            "intent",
            "unknown"
        )

        modules = self.get_modules(
            intent
        )

        return {
            "intent": intent,
            "confidence": intent_result.get(
                "confidence",
                0
            ),
            "entities": intent_result.get(
                "entities",
                []
            ),
            "modules": modules,
            "steps": self.build_steps(
                modules
            ),
            "status": "planned"
        }


    def add_route(
        self,
        intent,
        modules
    ):
        self.routes[intent] = modules

        return True


    def supported_routes(
        self
    ):
        return list(
            self.routes.keys()
        )
