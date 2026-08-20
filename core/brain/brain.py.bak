class Brain:

    def __init__(self, llm_gateway=None):

        self.llm_gateway = llm_gateway


    def understand(self, context):

        user_input = context.get(
            "user_input",
            ""
        )


        # 默认结果
        result = {
            "intent": "unknown",
            "goal": user_input,
            "entities": [],
            "confidence": 0.5
        }


        # LLM模式
        if self.llm_gateway:

            response = self.llm_gateway.generate(
                user_input
            )

            print("LLM Response:")
            print(response)


        # Rule fallback

        if "测试" in user_input:

            result["intent"] = "test_system"

            result["goal"] = user_input

            result["entities"] = [
                "AI-OS"
            ]

            result["confidence"] = 0.95


        elif "文件" in user_input:

            result["intent"] = "file_task"

            result["entities"] = [
                "文件"
            ]

            result["confidence"] = 0.8


        return result
