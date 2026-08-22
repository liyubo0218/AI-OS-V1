from .base_provider import BaseProvider


class MockProvider(BaseProvider):

    def __init__(self):
        super().__init__("mock")

    def generate(
        self,
        prompt,
        context=None
    ):
        return {
            "text": f"Mock response: {prompt}",
            "model": self.name,
            "confidence": 0.8,
            "status": "success"
        }
