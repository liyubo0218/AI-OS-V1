class MockModelAdapter:

    def __init__(self):

        self.model_name = "mock-llm"


    def generate(
        self,
        prompt,
        context=None
    ):

        return {
            "text":
                f"Mock response: {prompt}",

            "model":
                self.model_name,

            "confidence":
                0.8,

            "status":
                "success"
        }
