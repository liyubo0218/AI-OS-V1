import os

from ai_gateway.providers.base_provider import BaseProvider


class CloudProvider(BaseProvider):

    def __init__(self):

        super().__init__(
            "cloud-model"
        )

        self.api_key = os.getenv(
            "AIOS_MODEL_KEY"
        )


    def generate(self, prompt):

        if not self.api_key:

            return {
                "model": self.name,
                "response": (
                    "Cloud Provider 未配置API Key，"
                    "使用fallback模式: "
                    + prompt
                ),
                "mode": "fallback"
            }


        # 真实API调用位置

        return {
            "model": self.name,
            "response": (
                "Cloud Provider 请求成功: "
                + prompt
            ),
            "mode": "cloud"
        }
