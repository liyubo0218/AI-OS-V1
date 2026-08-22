from core.brain.providers.base_provider import BaseProvider


class MockProvider(BaseProvider):

    def __init__(self):

        super().__init__(
            "mock-model"
        )


    def generate(self, prompt):

        return {
            "model": self.name,
            "response": (
                "模型响应: "
                + prompt
            )
        }
