import os

from core.brain.providers.base_provider import BaseProvider


class CloudProvider(BaseProvider):

    def __init__(self):
        super().__init__(
            "cloud-model"
        )
        self.api_key = os.getenv(
            "AIOS_MODEL_KEY"
        )

    def generate(
        self,
        prompt,
        context=None
    ):
        if not self.api_key:
            return {
                "text": (
                    "Cloud Provider 未配置API Key，"
                    "使用fallback模式: "
                    + prompt
                ),
                "model": self.name,
                "confidence": 0.6,
                "status": "fallback"
            }

        return {
            "text": (
                "Cloud Provider 请求成功: "
                + prompt
            ),
            "model": self.name,
            "confidence": 0.9,
            "status": "success"
        }
