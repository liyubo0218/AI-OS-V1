from .base_provider import BaseProvider


class MockProvider(BaseProvider):

    def __init__(self):

        self.model_name = "mock-provider"


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
