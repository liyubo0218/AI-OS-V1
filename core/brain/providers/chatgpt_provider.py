from core.brain.providers.base_provider import BaseProvider

from .chatgpt.protocol import ChatGPTBridge

from .chatgpt.request import ChatGPTRequest



class ChatGPTProvider(BaseProvider):


    def __init__(self):

        super().__init__(
            "chatgpt-model"
        )

        self.bridge = ChatGPTBridge()



    def generate(
        self,
        prompt
    ):

        request = ChatGPTRequest(
            "llm_request_001",
            prompt
        )


        result = self.bridge.chat(
            request
        )


        return {
            "model": self.name,
            "response": result["response"],
            "mode": "bridge"
        }
