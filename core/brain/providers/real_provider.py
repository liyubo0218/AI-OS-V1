from core.brain.providers.base_provider import BaseProvider


class RealProvider(BaseProvider):

    def __init__(self):

        super().__init__(
            "real-model"
        )


    def generate(self, prompt, context=None):

        return {
            "model": self.name,
            "response": (
                "Real Provider 收到请求: "
                + prompt
            )
        }
